bernardoNotifyMailTorrentCompletionDeluge
=========================================

Notified through a mail to complete the download of a torrent.

 The Execute plugin is only supported from deluge versions 1.3RC2 and up. It gives you the option to run script notify_mail_torrent_completion.p events in Deluge (Event complete:when a torrent has finished downloading).

The script to be executed will be supplied with three Torrent variables:

    ID (Hash)
    Name
    Folder
        
Enable the plugin in the Plugins menu in Preferences. For the webUI; reopen the Preferences menu for the Execute plugin to be available.

Note: After enabling this plugin Deluge may require restarted for it to work properly.

The events Torrent Complete can be selected and the full path to the script entered (e.g. /home/user/notify_mail_torrent_completion.py)         

<img src="https://raw.github.com/bernardosecades/bernardoNotifyMailTorrentCompletionDeluge/master/screenshot.png" />

Make sure the script is set to executable: 

chmod u+x /home/user/notify_mail_torrent_completion.py
