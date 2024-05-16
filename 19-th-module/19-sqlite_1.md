```
C:\Users\Stas\PycharmProjects\Practice>sqlite3
SQLite version 3.45.3 2024-04-15 13:34:05 (UTF-16 console I/O)
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> open database.db
   ...> ;
Parse error: near "open": syntax error
  open database.db ;
  ^--- error here
sqlite> .help
.archive ...             Manage SQL archives
.auth ON|OFF             Show authorizer callbacks
.backup ?DB? FILE        Backup DB (default "main") to FILE
.bail on|off             Stop after hitting an error.  Default OFF
.cd DIRECTORY            Change the working directory to DIRECTORY
.changes on|off          Show number of rows changed by SQL
.check GLOB              Fail if output since .testcase does not match
.clone NEWDB             Clone data into NEWDB from the existing database
.connection [close] [#]  Open or close an auxiliary database connection
.crnl on|off             Translate \n to \r\n.  Default ON
.databases               List names and files of attached databases
.dbconfig ?op? ?val?     List or change sqlite3_db_config() options
.dbinfo ?DB?             Show status information about the database
.dump ?OBJECTS?          Render database content as SQL
.echo on|off             Turn command echo on or off
.eqp on|off|full|...     Enable or disable automatic EXPLAIN QUERY PLAN
.excel                   Display the output of next command in spreadsheet
.exit ?CODE?             Exit this program with return-code CODE
.expert                  EXPERIMENTAL. Suggest indexes for queries
.explain ?on|off|auto?   Change the EXPLAIN formatting mode.  Default: auto
.filectrl CMD ...        Run various sqlite3_file_control() operations
.fullschema ?--indent?   Show schema and the content of sqlite_stat tables
.headers on|off          Turn display of headers on or off
.help ?-all? ?PATTERN?   Show help text for PATTERN
.import FILE TABLE       Import data from FILE into TABLE
.indexes ?TABLE?         Show names of indexes
.limit ?LIMIT? ?VAL?     Display or change the value of an SQLITE_LIMIT
.lint OPTIONS            Report potential schema issues.
.load FILE ?ENTRY?       Load an extension library
.log FILE|on|off         Turn logging on or off.  FILE can be stderr/stdout
.mode MODE ?OPTIONS?     Set output mode
.nonce STRING            Suspend safe mode for one command if nonce matches
.nullvalue STRING        Use STRING in place of NULL values
.once ?OPTIONS? ?FILE?   Output for the next SQL command only to FILE
.open ?OPTIONS? ?FILE?   Close existing database and reopen FILE
.output ?FILE?           Send output to FILE or stdout if FILE is omitted
.parameter CMD ...       Manage SQL parameter bindings
.print STRING...         Print literal STRING
.progress N              Invoke progress handler after every N opcodes
.prompt MAIN CONTINUE    Replace the standard prompts
.quit                    Stop interpreting input stream, exit if primary.
.read FILE               Read input from FILE or command output
.recover                 Recover as much data as possible from corrupt db.
.restore ?DB? FILE       Restore content of DB (default "main") from FILE
.save ?OPTIONS? FILE     Write database to FILE (an alias for .backup ...)
.scanstats on|off|est    Turn sqlite3_stmt_scanstatus() metrics on or off
.schema ?PATTERN?        Show the CREATE statements matching PATTERN
.separator COL ?ROW?     Change the column and row separators
.session ?NAME? CMD ...  Create or control sessions
.sha3sum ...             Compute a SHA3 hash of database content
.shell CMD ARGS...       Run CMD ARGS... in a system shell
.show                    Show the current values for various settings
.stats ?ARG?             Show stats or turn stats on or off
.system CMD ARGS...      Run CMD ARGS... in a system shell
.tables ?TABLE?          List names of tables matching LIKE pattern TABLE
.timeout MS              Try opening locked tables for MS milliseconds
.timer on|off            Turn SQL timer on or off
.trace ?OPTIONS?         Output each SQL statement as it is run
.version                 Show source, library and compiler versions
.vfsinfo ?AUX?           Information about the top-level VFS
.vfslist                 List all available VFSes
.vfsname ?AUX?           Print the name of the VFS stack
.width NUM1 NUM2 ...     Set minimum column widths for columnar output
sqlite> read database,db
   ...> ;
Parse error: near "read": syntax error
  read database,db ;
  ^--- error here
sqlite> .open database.db
sqlite> CREATE TABLE students(id INTEGER PRIMARY KEY AUTOINCREMENT,
(x1...> name TEXT NOT NULL,
(x1...> surname TEXT NOT NULL);
sqlite> INSERT INTO students (name, surname) VALUES ('Иван', 'Петров');
sqlite> INSERT INTO students (name, surname) VALUES ('Петр', 'Петров'); 
sqlite> INSERT INTO students (name, surname) VALUES ('Анна', 'Аннова'); 
sqlite> SELECT * FROM students;
1|Иван|Петров
2|Петр|Петров
3|Анна|Аннова
sqlite> .headers on
sqlite> SELECT * FROM students;
id|name|surname
1|Иван|Петров
2|Петр|Петров
3|Анна|Аннова
sqlite> .mode box                                                       
sqlite> SELECT * FROM students;
┌────┬──────┬─────────┐
│ id │ name │ surname │
├────┼──────┼─────────┤
│ 1  │ Иван │ Петров  │
│ 2  │ Петр │ Петров  │
│ 3  │ Анна │ Аннова  │
└────┴──────┴─────────┘
sqlite> SELECT id, surname FROM students WHERE id > 1;
┌────┬─────────┐
│ id │ surname │
├────┼─────────┤
│ 2  │ Петров  │
│ 3  │ Аннова  │
└────┴─────────┘
sqlite> SELECT id, surname FROM students WHERE id > 1 AND surname LIKE '%ова';
┌────┬─────────┐
│ id │ surname │
├────┼─────────┤
│ 3  │ Аннова  │
└────┴─────────┘
sqlite> UPDATE students SET surname = 'Петрова' WHERE id = 3;
sqlite> SELECT * FROM students;                        
┌────┬──────┬─────────┐
│ id │ name │ surname │
├────┼──────┼─────────┤
│ 1  │ Иван │ Петров  │
│ 2  │ Петр │ Петров  │
│ 3  │ Анна │ Петрова │
└────┴──────┴─────────┘
sqlite> DELETE FROM students WHERE id = 1;
sqlite> SELECT * FROM students;
┌────┬──────┬─────────┐
│ id │ name │ surname │
├────┼──────┼─────────┤
│ 2  │ Петр │ Петров  │
│ 3  │ Анна │ Петрова │
└────┴──────┴─────────┘
sqlite> ^D
   ...> .quit
   ...> ;
Parse error: unrecognized token: ""
   .quit ;
  ^--- error here
sqlite> .quit

C:\Users\Stas\PycharmProjects\Practice>

```