#!/usr/bin/python3

import mysql.connector
import vlc
import os,sys,time

"""
CREATE TABLE `skeletor`.`Actions` ( `Move` INT NOT NULL DEFAULT '0' , `Howl` INT NOT NULL DEFAULT '0' , `Blink` INT NOT NULL DEFAULT '0' , `Click` INT NOT NULL , `Epoq` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , `Photo` INT NOT NULL , `Quit` INT NOT NULL DEFAULT '0' , `Start` INT NOT NULL DEFAULT '0' , `Detect` INT NOT NULL DEFAULT '0' ) ENGINE = InnoDB; 
"""

class skeleplay():
    def __init__(self):
        self.db_name  = "skeletor"
        self.db_table = "radiohead"
        self.db =  mysql.connector.connect(user='root', 
                                           password='pass1234',
                                           host='127.0.0.1',
                                           database=self.db_name)

    def create_database(self):
        #  Check if exists
        self.db_ptr = self.db.cursor()
        self.db_ptr.execute(f"""SELECT count(*) FROM information_schema.TABLES WHERE (TABLE_SCHEMA = '{self.db_name}') AND (TABLE_NAME = '{self.db_table}')""")
        results = self.db_ptr.fetchall()[0][0]
        self.db.commit()
        if results:
            print(f"Database:table {self.db_name}:{self.db_table} already exists. No need to recreate.")
            return
        
        self.db_ptr.execute(f"""CREATE TABLE `{self.db_name}`.`{self.db_table}` ( `mp3` LONGTEXT NULL DEFAULT NULL , `timestamp` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ) ENGINE = InnoDB;""")
        """ALTER TABLE `radiohead` ADD `Status` TINYINT NULL DEFAULT '0' AFTER `mp3`;"""

        self.db.commit()

    def clean_database(self):
        sql_query = f"""DELETE FROM {self.db_table} WHERE NOT mp3 LIKE '%http://%';"""
        self.db.cursor().execute(sql_query)
        
    def read_database(self):
        # Assume it exists...
        
        self.db_ptr = self.db.cursor()
        self.db_ptr.execute(f"SELECT mp3,timestamp from {self.db_table}")
        for mp3, timestamp in self.db_ptr:
            print(timestamp, mp3)
        self.db.commit()

    def play_stream(self, stream="https://sverigesradio.se/topsy/ljudfil/srse/9534994.mp3"):
        # Thread
        print("Play stream")
        try:
            self.player = vlc.MediaPlayer(stream)
        except:
            print(f"{stream} not found!")
            return
        
        self.player.play()
        self.player.get_instance()        
        playing = set([1])
        time.sleep(1.5) # startup time.        
        duration = self.player.get_length() / 1000
        while duration > 0:
            song_time = self.player.get_state()
            time.sleep(5) # if 1, then delay is 1 second.
            duration = duration - 5
            print(duration)
            print(self.player.is_playing())        

def main():
    radiohead = skeleplay()
    radiohead.create_database()
    radiohead.read_database()
    radiohead.clean_database()
    radiohead.play_stream()
    

if __name__ == "__main__":
    main()

