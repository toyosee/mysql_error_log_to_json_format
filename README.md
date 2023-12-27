Have you always wanted to convert errors in your mysql error log file to a structured data format.
This might be for use in database or APIs.
Mysql Version 5.7 does not have the functionality to export errors as JSON, this is available in version 8
This script will do the magic for you irrespective of the version of mysql
You need to run the script entering the path to your error file and it will generate a JSON format of the error file.
Please note: you might need to tweak the regular expression if you are not getting the desired result.
Currently, this is the structure of the RE:
    (\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}): Matches the timestamp format in "YYYY-MM-DD HH:MM:SS" format.
    ([\da-fA-F]+): Matches the process ID, assuming it's represented by hexadecimal characters.
    (\w+): Matches the component (such as 'InnoDB', 'Note', etc.).
    :\s+: Matches the colon and any following whitespace.
    ([\s\S]*?): Matches the message content (any character, including newline, in non-greedy mode).
    (?=\n\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}|$): Positive lookahead to ensure the match stops at the next log entry (timestamp format) or end of the string.

Feel free to use and adjust, Send in your comments and suggestions.
