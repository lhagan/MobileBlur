# encoding utf-8

__author__ = "Thadeus Burgess <thadeusb@thadeusb.com>"

#    we classify as "non-reserved" those key words that are explicitly known
#    to the parser but are allowed as column or table names. Some key words
#    that are otherwise non-reserved cannot be used as function or data type n
#    ames and are in the nonreserved list. (Most of these words represent
#    built-in functions or data types with special syntax. The function
#    or type is still available but it cannot be redefined by the user.)
#    Labeled "reserved" are those tokens that are not allowed as column or
#    table names. Some reserved key words are allowable as names for
#    functions or data typesself.

# Note at the bottom of the list is a dict containing references to the
# tuples, and also if you add a list don't forget to remove its default
# set of COMMON.

# Keywords that are adapter specific. Such as a list of "postgresql"
# or "mysql" keywords

# These are keywords that are common to all SQL dialects, and should
# never be used as a table or column. Even if you use one of these
# the cursor will throw an OperationalError for the SQL syntax.
COMMON = set((
    'SELECT',
    'INSERT',
    'DELETE',
    'UPDATE',
    'DROP',
    'CREATE',
    'ALTER',

    'WHERE',
    'FROM',
    'INNER',
    'JOIN',
    'AND',
    'OR',
    'LIKE',
    'ON',
    'IN',
    'SET',

    'BY',
    'GROUP',
    'ORDER',
    'LEFT',
    'OUTER',

    'IF',
    'END',
    'THEN',
    'LOOP',
    'AS',
    'ELSE',
    'FOR',

    'CASE',
    'WHEN',
    'MIN',
    'MAX',
    'DISTINCT',
))


POSTGRESQL = set((
    'FALSE',
    'TRUE',
    'ALL',
    'ANALYSE',
    'ANALYZE',
    'AND',
    'ANY',
    'ARRAY',
    'AS',
    'ASC',
    'ASYMMETRIC',
    'AUTHORIZATION',
    'BETWEEN',
    'BIGINT',
    'BINARY',
    'BIT',
    'BOOLEAN',
    'BOTH',
    'CASE',
    'CAST',
    'CHAR',
    'CHARACTER',
    'CHECK',
    'COALESCE',
    'COLLATE',
    'COLUMN',
    'CONSTRAINT',
    'CREATE',
    'CROSS',
    'CURRENT_CATALOG',
    'CURRENT_DATE',
    'CURRENT_ROLE',
    'CURRENT_SCHEMA',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'CURRENT_USER',
    'DEC',
    'DECIMAL',
    'DEFAULT',
    'DEFERRABLE',
    'DESC',
    'DISTINCT',
    'DO',
    'ELSE',
    'END',
    'EXCEPT',
    'EXISTS',
    'EXTRACT',
    'FETCH',
    'FLOAT',
    'FOR',
    'FOREIGN',
    'FREEZE',
    'FROM',
    'FULL',
    'GRANT',
    'GREATEST',
    'GROUP',
    'HAVING',
    'ILIKE',
    'IN',
    'INITIALLY',
    'INNER',
    'INOUT',
    'INT',
    'INTEGER',
    'INTERSECT',
    'INTERVAL',
    'INTO',
    'IS',
    'ISNULL',
    'JOIN',
    'LEADING',
    'LEAST',
    'LEFT',
    'LIKE',
    'LIMIT',
    'LOCALTIME',
    'LOCALTIMESTAMP',
    'NATIONAL',
    'NATURAL',
    'NCHAR',
    'NEW',
    'NONE',
    'NOT',
    'NOTNULL',
    'NULL',
    'NULLIF',
    'NUMERIC',
    'OFF',
    'OFFSET',
    'OLD',
    'ON',
    'ONLY',
    'OR',
    'ORDER',
    'OUT',
    'OUTER',
    'OVERLAPS',
    'OVERLAY',
    'PLACING',
    'POSITION',
    'PRECISION',
    'PRIMARY',
    'REAL',
    'REFERENCES',
    'RETURNING',
    'RIGHT',
    'ROW',
    'SELECT',
    'SESSION_USER',
    'SETOF',
    'SIMILAR',
    'SMALLINT',
    'SOME',
    'SUBSTRING',
    'SYMMETRIC',
    'TABLE',
    'THEN',
    'TIME',
    'TIMESTAMP',
    'TO',
    'TRAILING',
    'TREAT',
    'TRIM',
    'UNION',
    'UNIQUE',
    'USER',
    'USING',
    'VALUES',
    'VARCHAR',
    'VARIADIC',
    'VERBOSE',
    'WHEN',
    'WHERE',
    'WITH',
    'XMLATTRIBUTES',
    'XMLCONCAT',
    'XMLELEMENT',
    'XMLFOREST',
    'XMLPARSE',
    'XMLPI',
    'XMLROOT',
    'XMLSERIALIZE',
))


POSTGRESQL_NONRESERVED = set((
    'A',
    'ABORT',
    'ABS',
    'ABSENT',
    'ABSOLUTE',
    'ACCESS',
    'ACCORDING',
    'ACTION',
    'ADA',
    'ADD',
    'ADMIN',
    'AFTER',
    'AGGREGATE',
    'ALIAS',
    'ALLOCATE',
    'ALSO',
    'ALTER',
    'ALWAYS',
    'ARE',
    'ARRAY_AGG',
    'ASENSITIVE',
    'ASSERTION',
    'ASSIGNMENT',
    'AT',
    'ATOMIC',
    'ATTRIBUTE',
    'ATTRIBUTES',
    'AVG',
    'BACKWARD',
    'BASE64',
    'BEFORE',
    'BEGIN',
    'BERNOULLI',
    'BIT_LENGTH',
    'BITVAR',
    'BLOB',
    'BOM',
    'BREADTH',
    'BY',
    'C',
    'CACHE',
    'CALL',
    'CALLED',
    'CARDINALITY',
    'CASCADE',
    'CASCADED',
    'CATALOG',
    'CATALOG_NAME',
    'CEIL',
    'CEILING',
    'CHAIN',
    'CHAR_LENGTH',
    'CHARACTER_LENGTH',
    'CHARACTER_SET_CATALOG',
    'CHARACTER_SET_NAME',
    'CHARACTER_SET_SCHEMA',
    'CHARACTERISTICS',
    'CHARACTERS',
    'CHECKED',
    'CHECKPOINT',
    'CLASS',
    'CLASS_ORIGIN',
    'CLOB',
    'CLOSE',
    'CLUSTER',
    'COBOL',
    'COLLATION',
    'COLLATION_CATALOG',
    'COLLATION_NAME',
    'COLLATION_SCHEMA',
    'COLLECT',
    'COLUMN_NAME',
    'COLUMNS',
    'COMMAND_FUNCTION',
    'COMMAND_FUNCTION_CODE',
    'COMMENT',
    'COMMIT',
    'COMMITTED',
    'COMPLETION',
    'CONCURRENTLY',
    'CONDITION',
    'CONDITION_NUMBER',
    'CONFIGURATION',
    'CONNECT',
    'CONNECTION',
    'CONNECTION_NAME',
    'CONSTRAINT_CATALOG',
    'CONSTRAINT_NAME',
    'CONSTRAINT_SCHEMA',
    'CONSTRAINTS',
    'CONSTRUCTOR',
    'CONTAINS',
    'CONTENT',
    'CONTINUE',
    'CONVERSION',
    'CONVERT',
    'COPY',
    'CORR',
    'CORRESPONDING',
    'COST',
    'COUNT',
    'COVAR_POP',
    'COVAR_SAMP',
    'CREATEDB',
    'CREATEROLE',
    'CREATEUSER',
    'CSV',
    'CUBE',
    'CUME_DIST',
    'CURRENT',
    'CURRENT_DEFAULT_TRANSFORM_GROUP',
    'CURRENT_PATH',
    'CURRENT_TRANSFORM_GROUP_FOR_TYPE',
    'CURSOR',
    'CURSOR_NAME',
    'CYCLE',
    'DATA',
    'DATABASE',
    'DATE',
    'DATETIME_INTERVAL_CODE',
    'DATETIME_INTERVAL_PRECISION',
    'DAY',
    'DEALLOCATE',
    'DECLARE',
    'DEFAULTS',
    'DEFERRED',
    'DEFINED',
    'DEFINER',
    'DEGREE',
    'DELETE',
    'DELIMITER',
    'DELIMITERS',
    'DENSE_RANK',
    'DEPTH',
    'DEREF',
    'DERIVED',
    'DESCRIBE',
    'DESCRIPTOR',
    'DESTROY',
    'DESTRUCTOR',
    'DETERMINISTIC',
    'DIAGNOSTICS',
    'DICTIONARY',
    'DISABLE',
    'DISCARD',
    'DISCONNECT',
    'DISPATCH',
    'DOCUMENT',
    'DOMAIN',
    'DOUBLE',
    'DROP',
    'DYNAMIC',
    'DYNAMIC_FUNCTION',
    'DYNAMIC_FUNCTION_CODE',
    'EACH',
    'ELEMENT',
    'EMPTY',
    'ENABLE',
    'ENCODING',
    'ENCRYPTED',
    'END-EXEC',
    'ENUM',
    'EQUALS',
    'ESCAPE',
    'EVERY',
    'EXCEPTION',
    'EXCLUDE',
    'EXCLUDING',
    'EXCLUSIVE',
    'EXEC',
    'EXECUTE',
    'EXISTING',
    'EXP',
    'EXPLAIN',
    'EXTERNAL',
    'FAMILY',
    'FILTER',
    'FINAL',
    'FIRST',
    'FIRST_VALUE',
    'FLAG',
    'FLOOR',
    'FOLLOWING',
    'FORCE',
    'FORTRAN',
    'FORWARD',
    'FOUND',
    'FREE',
    'FUNCTION',
    'FUSION',
    'G',
    'GENERAL',
    'GENERATED',
    'GET',
    'GLOBAL',
    'GO',
    'GOTO',
    'GRANTED',
    'GROUPING',
    'HANDLER',
    'HEADER',
    'HEX',
    'HIERARCHY',
    'HOLD',
    'HOST',
    'HOUR',
#    'ID',
    'IDENTITY',
    'IF',
    'IGNORE',
    'IMMEDIATE',
    'IMMUTABLE',
    'IMPLEMENTATION',
    'IMPLICIT',
    'INCLUDING',
    'INCREMENT',
    'INDENT',
    'INDEX',
    'INDEXES',
    'INDICATOR',
    'INFIX',
    'INHERIT',
    'INHERITS',
    'INITIALIZE',
    'INPUT',
    'INSENSITIVE',
    'INSERT',
    'INSTANCE',
    'INSTANTIABLE',
    'INSTEAD',
    'INTERSECTION',
    'INVOKER',
    'ISOLATION',
    'ITERATE',
    'K',
    'KEY',
    'KEY_MEMBER',
    'KEY_TYPE',
    'LAG',
    'LANCOMPILER',
    'LANGUAGE',
    'LARGE',
    'LAST',
    'LAST_VALUE',
    'LATERAL',
    'LC_COLLATE',
    'LC_CTYPE',
    'LEAD',
    'LENGTH',
    'LESS',
    'LEVEL',
    'LIKE_REGEX',
    'LISTEN',
    'LN',
    'LOAD',
    'LOCAL',
    'LOCATION',
    'LOCATOR',
    'LOCK',
    'LOGIN',
    'LOWER',
    'M',
    'MAP',
    'MAPPING',
    'MATCH',
    'MATCHED',
    'MAX',
    'MAX_CARDINALITY',
    'MAXVALUE',
    'MEMBER',
    'MERGE',
    'MESSAGE_LENGTH',
    'MESSAGE_OCTET_LENGTH',
    'MESSAGE_TEXT',
    'METHOD',
    'MIN',
    'MINUTE',
    'MINVALUE',
    'MOD',
    'MODE',
    'MODIFIES',
    'MODIFY',
    'MODULE',
    'MONTH',
    'MORE',
    'MOVE',
    'MULTISET',
    'MUMPS',
#    'NAME',
    'NAMES',
    'NAMESPACE',
    'NCLOB',
    'NESTING',
    'NEXT',
    'NFC',
    'NFD',
    'NFKC',
    'NFKD',
    'NIL',
    'NO',
    'NOCREATEDB',
    'NOCREATEROLE',
    'NOCREATEUSER',
    'NOINHERIT',
    'NOLOGIN',
    'NORMALIZE',
    'NORMALIZED',
    'NOSUPERUSER',
    'NOTHING',
    'NOTIFY',
    'NOWAIT',
    'NTH_VALUE',
    'NTILE',
    'NULLABLE',
    'NULLS',
    'NUMBER',
    'OBJECT',
    'OCCURRENCES_REGEX',
    'OCTET_LENGTH',
    'OCTETS',
    'OF',
    'OIDS',
    'OPEN',
    'OPERATION',
    'OPERATOR',
    'OPTION',
    'OPTIONS',
    'ORDERING',
    'ORDINALITY',
    'OTHERS',
    'OUTPUT',
    'OVER',
    'OVERRIDING',
    'OWNED',
    'OWNER',
    'P',
    'PAD',
    'PARAMETER',
    'PARAMETER_MODE',
    'PARAMETER_NAME',
    'PARAMETER_ORDINAL_POSITION',
    'PARAMETER_SPECIFIC_CATALOG',
    'PARAMETER_SPECIFIC_NAME',
    'PARAMETER_SPECIFIC_SCHEMA',
    'PARAMETERS',
    'PARSER',
    'PARTIAL',
    'PARTITION',
    'PASCAL',
    'PASSING',
#    'PASSWORD',
    'PATH',
    'PERCENT_RANK',
    'PERCENTILE_CONT',
    'PERCENTILE_DISC',
    'PLANS',
    'PLI',
    'POSITION_REGEX',
    'POSTFIX',
    'POWER',
    'PRECEDING',
    'PREFIX',
    'PREORDER',
    'PREPARE',
    'PREPARED',
    'PRESERVE',
    'PRIOR',
    'PRIVILEGES',
    'PROCEDURAL',
    'PROCEDURE',
    'PUBLIC',
    'QUOTE',
    'RANGE',
    'RANK',
    'READ',
    'READS',
    'REASSIGN',
    'RECHECK',
    'RECURSIVE',
    'REF',
    'REFERENCING',
    'REGR_AVGX',
    'REGR_AVGY',
    'REGR_COUNT',
    'REGR_INTERCEPT',
    'REGR_R2',
    'REGR_SLOPE',
    'REGR_SXX',
    'REGR_SXY',
    'REGR_SYY',
    'REINDEX',
    'RELATIVE',
    'RELEASE',
    'RENAME',
    'REPEATABLE',
    'REPLACE',
    'REPLICA',
    'RESET',
    'RESPECT',
    'RESTART',
    'RESTRICT',
    'RESULT',
    'RETURN',
    'RETURNED_CARDINALITY',
    'RETURNED_LENGTH',
    'RETURNED_OCTET_LENGTH',
    'RETURNED_SQLSTATE',
    'RETURNS',
    'REVOKE',
#    'ROLE',
    'ROLLBACK',
    'ROLLUP',
    'ROUTINE',
    'ROUTINE_CATALOG',
    'ROUTINE_NAME',
    'ROUTINE_SCHEMA',
    'ROW_COUNT',
    'ROW_NUMBER',
    'ROWS',
    'RULE',
    'SAVEPOINT',
    'SCALE',
    'SCHEMA',
    'SCHEMA_NAME',
    'SCOPE',
    'SCOPE_CATALOG',
    'SCOPE_NAME',
    'SCOPE_SCHEMA',
    'SCROLL',
    'SEARCH',
    'SECOND',
    'SECTION',
    'SECURITY',
    'SELF',
    'SENSITIVE',
    'SEQUENCE',
    'SERIALIZABLE',
    'SERVER',
    'SERVER_NAME',
    'SESSION',
    'SET',
    'SETS',
    'SHARE',
    'SHOW',
    'SIMPLE',
    'SIZE',
    'SOURCE',
    'SPACE',
    'SPECIFIC',
    'SPECIFIC_NAME',
    'SPECIFICTYPE',
    'SQL',
    'SQLCODE',
    'SQLERROR',
    'SQLEXCEPTION',
    'SQLSTATE',
    'SQLWARNING',
    'SQRT',
    'STABLE',
    'STANDALONE',
    'START',
    'STATE',
    'STATEMENT',
    'STATIC',
    'STATISTICS',
    'STDDEV_POP',
    'STDDEV_SAMP',
    'STDIN',
    'STDOUT',
    'STORAGE',
    'STRICT',
    'STRIP',
    'STRUCTURE',
    'STYLE',
    'SUBCLASS_ORIGIN',
    'SUBLIST',
    'SUBMULTISET',
    'SUBSTRING_REGEX',
    'SUM',
    'SUPERUSER',
    'SYSID',
    'SYSTEM',
    'SYSTEM_USER',
    'T',
#    'TABLE_NAME',
    'TABLESAMPLE',
    'TABLESPACE',
    'TEMP',
    'TEMPLATE',
    'TEMPORARY',
    'TERMINATE',
    'TEXT',
    'THAN',
    'TIES',
    'TIMEZONE_HOUR',
    'TIMEZONE_MINUTE',
    'TOP_LEVEL_COUNT',
    'TRANSACTION',
    'TRANSACTION_ACTIVE',
    'TRANSACTIONS_COMMITTED',
    'TRANSACTIONS_ROLLED_BACK',
    'TRANSFORM',
    'TRANSFORMS',
    'TRANSLATE',
    'TRANSLATE_REGEX',
    'TRANSLATION',
    'TRIGGER',
    'TRIGGER_CATALOG',
    'TRIGGER_NAME',
    'TRIGGER_SCHEMA',
    'TRIM_ARRAY',
    'TRUNCATE',
    'TRUSTED',
    'TYPE',
    'UESCAPE',
    'UNBOUNDED',
    'UNCOMMITTED',
    'UNDER',
    'UNENCRYPTED',
    'UNKNOWN',
    'UNLISTEN',
    'UNNAMED',
    'UNNEST',
    'UNTIL',
    'UNTYPED',
    'UPDATE',
    'UPPER',
    'URI',
    'USAGE',
    'USER_DEFINED_TYPE_CATALOG',
    'USER_DEFINED_TYPE_CODE',
    'USER_DEFINED_TYPE_NAME',
    'USER_DEFINED_TYPE_SCHEMA',
    'VACUUM',
    'VALID',
    'VALIDATOR',
    'VALUE',
    'VAR_POP',
    'VAR_SAMP',
    'VARBINARY',
    'VARIABLE',
    'VARYING',
    'VERSION',
    'VIEW',
    'VOLATILE',
    'WHENEVER',
    'WHITESPACE',
    'WIDTH_BUCKET',
    'WINDOW',
    'WITHIN',
    'WITHOUT',
    'WORK',
    'WRAPPER',
    'WRITE',
    'XML',
    'XMLAGG',
    'XMLBINARY',
    'XMLCAST',
    'XMLCOMMENT',
    'XMLDECLARATION',
    'XMLDOCUMENT',
    'XMLEXISTS',
    'XMLITERATE',
    'XMLNAMESPACES',
    'XMLQUERY',
    'XMLSCHEMA',
    'XMLTABLE',
    'XMLTEXT',
    'XMLVALIDATE',
    'YEAR',
    'YES',
    'ZONE',
))

#Thanks villas
FIREBIRD = set((
    'ABS',
    'ACTIVE',
    'ADMIN',
    'AFTER',
    'ASCENDING',
    'AUTO',
    'AUTODDL',
    'BASED',
    'BASENAME',
    'BASE_NAME',
    'BEFORE',
    'BIT_LENGTH',
    'BLOB',
    'BLOBEDIT',
    'BOOLEAN',
    'BOTH',
    'BUFFER',
    'CACHE',
    'CHAR_LENGTH',
    'CHARACTER_LENGTH',
    'CHECK_POINT_LEN',
    'CHECK_POINT_LENGTH',
    'CLOSE',
    'COMMITTED',
    'COMPILETIME',
    'COMPUTED',
    'CONDITIONAL',
    'CONNECT',
    'CONTAINING',
    'CROSS',
    'CSTRING',
    'CURRENT_CONNECTION',
    'CURRENT_ROLE',
    'CURRENT_TRANSACTION',
    'CURRENT_USER',
    'DATABASE',
    'DB_KEY',
    'DEBUG',
    'DESCENDING',
    'DISCONNECT',
    'DISPLAY',
    'DO',
    'ECHO',
    'EDIT',
    'ENTRY_POINT',
    'EVENT',
    'EXIT',
    'EXTERN',
    'FALSE',
    'FETCH',
    'FILE',
    'FILTER',
    'FREE_IT',
    'FUNCTION',
    'GDSCODE',
    'GENERATOR',
    'GEN_ID',
    'GLOBAL',
    'GROUP_COMMIT_WAIT',
    'GROUP_COMMIT_WAIT_TIME',
    'HELP',
    'IF',
    'INACTIVE',
    'INDEX',
    'INIT',
    'INPUT_TYPE',
    'INSENSITIVE',
    'ISQL',
    'LC_MESSAGES',
    'LC_TYPE',
    'LEADING',
    'LENGTH',
    'LEV',
    'LOGFILE',
    'LOG_BUFFER_SIZE',
    'LOG_BUF_SIZE',
    'LONG',
    'LOWER',
    'MANUAL',
    'MAXIMUM',
    'MAXIMUM_SEGMENT',
    'MAX_SEGMENT',
    'MERGE',
    'MESSAGE',
    'MINIMUM',
    'MODULE_NAME',
    'NOAUTO',
    'NUM_LOG_BUFS',
    'NUM_LOG_BUFFERS',
    'OCTET_LENGTH',
    'OPEN',
    'OUTPUT_TYPE',
    'OVERFLOW',
    'PAGE',
    'PAGELENGTH',
    'PAGES',
    'PAGE_SIZE',
    'PARAMETER',
#    'PASSWORD',
    'PLAN',
    'POST_EVENT',
    'QUIT',
    'RAW_PARTITIONS',
    'RDB$DB_KEY',
    'RECORD_VERSION',
    'RECREATE',
    'RECURSIVE',
    'RELEASE',
    'RESERV',
    'RESERVING',
    'RETAIN',
    'RETURN',
    'RETURNING_VALUES',
    'RETURNS',
#    'ROLE',
    'ROW_COUNT',
    'ROWS',
    'RUNTIME',
    'SAVEPOINT',
    'SECOND',
    'SENSITIVE',
    'SHADOW',
    'SHARED',
    'SHELL',
    'SHOW',
    'SINGULAR',
    'SNAPSHOT',
    'SORT',
    'STABILITY',
    'START',
    'STARTING',
    'STARTS',
    'STATEMENT',
    'STATIC',
    'STATISTICS',
    'SUB_TYPE',
    'SUSPEND',
    'TERMINATOR',
    'TRAILING',
    'TRIGGER',
    'TRIM',
    'TRUE',
    'TYPE',
    'UNCOMMITTED',
    'UNKNOWN',
    'USING',
    'VARIABLE',
    'VERSION',
    'WAIT',
    'WEEKDAY',
    'WHILE',
    'YEARDAY',
))
FIREBIRD_NONRESERVED = set((
    'BACKUP',
    'BLOCK',
    'COALESCE',
    'COLLATION',
    'COMMENT',
    'DELETING',
    'DIFFERENCE',
    'IIF',
    'INSERTING',
    'LAST',
    'LEAVE',
    'LOCK',
    'NEXT',
    'NULLIF',
    'NULLS',
    'RESTART',
    'RETURNING',
    'SCALAR_ARRAY',
    'SEQUENCE',
    'STATEMENT',
    'UPDATING',
    'ABS',
    'ACCENT',
    'ACOS',
    'ALWAYS',
    'ASCII_CHAR',
    'ASCII_VAL',
    'ASIN',
    'ATAN',
    'ATAN2',
    'BACKUP',
    'BIN_AND',
    'BIN_OR',
    'BIN_SHL',
    'BIN_SHR',
    'BIN_XOR',
    'BLOCK',
    'CEIL',
    'CEILING',
    'COLLATION',
    'COMMENT',
    'COS',
    'COSH',
    'COT',
    'DATEADD',
    'DATEDIFF',
    'DECODE',
    'DIFFERENCE',
    'EXP',
    'FLOOR',
    'GEN_UUID',
    'GENERATED',
    'HASH',
    'IIF',
    'LIST',
    'LN',
    'LOG',
    'LOG10',
    'LPAD',
    'MATCHED',
    'MATCHING',
    'MAXVALUE',
    'MILLISECOND',
    'MINVALUE',
    'MOD',
    'NEXT',
    'OVERLAY',
    'PAD',
    'PI',
    'PLACING',
    'POWER',
    'PRESERVE',
    'RAND',
    'REPLACE',
    'RESTART',
    'RETURNING',
    'REVERSE',
    'ROUND',
    'RPAD',
    'SCALAR_ARRAY',
    'SEQUENCE',
    'SIGN',
    'SIN',
    'SINH',
    'SPACE',
    'SQRT',
    'TAN',
    'TANH',
    'TEMPORARY',
    'TRUNC',
    'WEEK',
))

# Thanks Jonathan Lundell
MYSQL = set((
    'ACCESSIBLE',
    'ADD',
    'ALL',
    'ALTER',
    'ANALYZE',
    'AND',
    'AS',
    'ASC',
    'ASENSITIVE',
    'BEFORE',
    'BETWEEN',
    'BIGINT',
    'BINARY',
    'BLOB',
    'BOTH',
    'BY',
    'CALL',
    'CASCADE',
    'CASE',
    'CHANGE',
    'CHAR',
    'CHARACTER',
    'CHECK',
    'COLLATE',
    'COLUMN',
    'CONDITION',
    'CONSTRAINT',
    'CONTINUE',
    'CONVERT',
    'CREATE',
    'CROSS',
    'CURRENT_DATE',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'CURRENT_USER',
    'CURSOR',
    'DATABASE',
    'DATABASES',
    'DAY_HOUR',
    'DAY_MICROSECOND',
    'DAY_MINUTE',
    'DAY_SECOND',
    'DEC',
    'DECIMAL',
    'DECLARE',
    'DEFAULT',
    'DELAYED',
    'DELETE',
    'DESC',
    'DESCRIBE',
    'DETERMINISTIC',
    'DISTINCT',
    'DISTINCTROW',
    'DIV',
    'DOUBLE',
    'DROP',
    'DUAL',
    'EACH',
    'ELSE',
    'ELSEIF',
    'ENCLOSED',
    'ESCAPED',
    'EXISTS',
    'EXIT',
    'EXPLAIN',
    'FALSE',
    'FETCH',
    'FLOAT',
    'FLOAT4',
    'FLOAT8',
    'FOR',
    'FORCE',
    'FOREIGN',
    'FROM',
    'FULLTEXT',
    'GRANT',
    'GROUP',
    'HAVING',
    'HIGH_PRIORITY',
    'HOUR_MICROSECOND',
    'HOUR_MINUTE',
    'HOUR_SECOND',
    'IF',
    'IGNORE',
    'IGNORE_SERVER_IDS',
    'IGNORE_SERVER_IDS',
    'IN',
    'INDEX',
    'INFILE',
    'INNER',
    'INOUT',
    'INSENSITIVE',
    'INSERT',
    'INT',
    'INT1',
    'INT2',
    'INT3',
    'INT4',
    'INT8',
    'INTEGER',
    'INTERVAL',
    'INTO',
    'IS',
    'ITERATE',
    'JOIN',
    'KEY',
    'KEYS',
    'KILL',
    'LEADING',
    'LEAVE',
    'LEFT',
    'LIKE',
    'LIMIT',
    'LINEAR',
    'LINES',
    'LOAD',
    'LOCALTIME',
    'LOCALTIMESTAMP',
    'LOCK',
    'LONG',
    'LONGBLOB',
    'LONGTEXT',
    'LOOP',
    'LOW_PRIORITY',
    'MASTER_HEARTBEAT_PERIOD',
    'MASTER_HEARTBEAT_PERIOD',
    'MASTER_SSL_VERIFY_SERVER_CERT',
    'MATCH',
    'MAXVALUE',
    'MAXVALUE',
    'MEDIUMBLOB',
    'MEDIUMINT',
    'MEDIUMTEXT',
    'MIDDLEINT',
    'MINUTE_MICROSECOND',
    'MINUTE_SECOND',
    'MOD',
    'MODIFIES',
    'NATURAL',
    'NO_WRITE_TO_BINLOG',
    'NOT',
    'NULL',
    'NUMERIC',
    'ON',
    'OPTIMIZE',
    'OPTION',
    'OPTIONALLY',
    'OR',
    'ORDER',
    'OUT',
    'OUTER',
    'OUTFILE',
    'PRECISION',
    'PRIMARY',
    'PROCEDURE',
    'PURGE',
    'RANGE',
    'READ',
    'READ_WRITE',
    'READS',
    'REAL',
    'REFERENCES',
    'REGEXP',
    'RELEASE',
    'RENAME',
    'REPEAT',
    'REPLACE',
    'REQUIRE',
    'RESIGNAL',
    'RESIGNAL',
    'RESTRICT',
    'RETURN',
    'REVOKE',
    'RIGHT',
    'RLIKE',
    'SCHEMA',
    'SCHEMAS',
    'SECOND_MICROSECOND',
    'SELECT',
    'SENSITIVE',
    'SEPARATOR',
    'SET',
    'SHOW',
    'SIGNAL',
    'SIGNAL',
    'SMALLINT',
    'SPATIAL',
    'SPECIFIC',
    'SQL',
    'SQL_BIG_RESULT',
    'SQL_CALC_FOUND_ROWS',
    'SQL_SMALL_RESULT',
    'SQLEXCEPTION',
    'SQLSTATE',
    'SQLWARNING',
    'SSL',
    'STARTING',
    'STRAIGHT_JOIN',
    'TABLE',
    'TERMINATED',
    'THEN',
    'TINYBLOB',
    'TINYINT',
    'TINYTEXT',
    'TO',
    'TRAILING',
    'TRIGGER',
    'TRUE',
    'UNDO',
    'UNION',
    'UNIQUE',
    'UNLOCK',
    'UNSIGNED',
    'UPDATE',
    'USAGE',
    'USE',
    'USING',
    'UTC_DATE',
    'UTC_TIME',
    'UTC_TIMESTAMP',
    'VALUES',
    'VARBINARY',
    'VARCHAR',
    'VARCHARACTER',
    'VARYING',
    'WHEN',
    'WHERE',
    'WHILE',
    'WITH',
    'WRITE',
    'XOR',
    'YEAR_MONTH',
    'ZEROFILL',
))

MSSQL = set((
    'ADD',
    'ALL',
    'ALTER',
    'AND',
    'ANY',
    'AS',
    'ASC',
    'AUTHORIZATION',
    'BACKUP',
    'BEGIN',
    'BETWEEN',
    'BREAK',
    'BROWSE',
    'BULK',
    'BY',
    'CASCADE',
    'CASE',
    'CHECK',
    'CHECKPOINT',
    'CLOSE',
    'CLUSTERED',
    'COALESCE',
    'COLLATE',
    'COLUMN',
    'COMMIT',
    'COMPUTE',
    'CONSTRAINT',
    'CONTAINS',
    'CONTAINSTABLE',
    'CONTINUE',
    'CONVERT',
    'CREATE',
    'CROSS',
    'CURRENT',
    'CURRENT_DATE',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'CURRENT_USER',
    'CURSOR',
    'DATABASE',
    'DBCC',
    'DEALLOCATE',
    'DECLARE',
    'DEFAULT',
    'DELETE',
    'DENY',
    'DESC',
    'DISK',
    'DISTINCT',
    'DISTRIBUTED',
    'DOUBLE',
    'DROP',
    'DUMMY',
    'DUMP',
    'ELSE',
    'END',
    'ERRLVL',
    'ESCAPE',
    'EXCEPT',
    'EXEC',
    'EXECUTE',
    'EXISTS',
    'EXIT',
    'FETCH',
    'FILE',
    'FILLFACTOR',
    'FOR',
    'FOREIGN',
    'FREETEXT',
    'FREETEXTTABLE',
    'FROM',
    'FULL',
    'FUNCTION',
    'GOTO',
    'GRANT',
    'GROUP',
    'HAVING',
    'HOLDLOCK',
    'IDENTITY',
    'IDENTITY_INSERT',
    'IDENTITYCOL',
    'IF',
    'IN',
    'INDEX',
    'INNER',
    'INSERT',
    'INTERSECT',
    'INTO',
    'IS',
    'JOIN',
    'KEY',
    'KILL',
    'LEFT',
    'LIKE',
    'LINENO',
    'LOAD',
    'NATIONAL ',
    'NOCHECK',
    'NONCLUSTERED',
    'NOT',
    'NULL',
    'NULLIF',
    'OF',
    'OFF',
    'OFFSETS',
    'ON',
    'OPEN',
    'OPENDATASOURCE',
    'OPENQUERY',
    'OPENROWSET',
    'OPENXML',
    'OPTION',
    'OR',
    'ORDER',
    'OUTER',
    'OVER',
    'PERCENT',
    'PLAN',
    'PRECISION',
    'PRIMARY',
    'PRINT',
    'PROC',
    'PROCEDURE',
    'PUBLIC',
    'RAISERROR',
    'READ',
    'READTEXT',
    'RECONFIGURE',
    'REFERENCES',
    'REPLICATION',
    'RESTORE',
    'RESTRICT',
    'RETURN',
    'REVOKE',
    'RIGHT',
    'ROLLBACK',
    'ROWCOUNT',
    'ROWGUIDCOL',
    'RULE',
    'SAVE',
    'SCHEMA',
    'SELECT',
    'SESSION_USER',
    'SET',
    'SETUSER',
    'SHUTDOWN',
    'SOME',
    'STATISTICS',
    'SYSTEM_USER',
    'TABLE',
    'TEXTSIZE',
    'THEN',
    'TO',
    'TOP',
    'TRAN',
    'TRANSACTION',
    'TRIGGER',
    'TRUNCATE',
    'TSEQUAL',
    'UNION',
    'UNIQUE',
    'UPDATE',
    'UPDATETEXT',
    'USE',
    'USER',
    'VALUES',
    'VARYING',
    'VIEW',
    'WAITFOR',
    'WHEN',
    'WHERE',
    'WHILE',
    'WITH',
    'WRITETEXT',
))

ORACLE = set((
    'ACCESS',
    'ADD',
    'ALL',
    'ALTER',
    'AND',
    'ANY',
    'AS',
    'ASC',
    'AUDIT',
    'BETWEEN',
    'BY',
    'CHAR',
    'CHECK',
    'CLUSTER',
    'COLUMN',
    'COMMENT',
    'COMPRESS',
    'CONNECT',
    'CREATE',
    'CURRENT',
    'DATE',
    'DECIMAL',
    'DEFAULT',
    'DELETE',
    'DESC',
    'DISTINCT',
    'DROP',
    'ELSE',
    'EXCLUSIVE',
    'EXISTS',
    'FILE',
    'FLOAT',
    'FOR',
    'FROM',
    'GRANT',
    'GROUP',
    'HAVING',
    'IDENTIFIED',
    'IMMEDIATE',
    'IN',
    'INCREMENT',
    'INDEX',
    'INITIAL',
    'INSERT',
    'INTEGER',
    'INTERSECT',
    'INTO',
    'IS',
    'LEVEL',
    'LIKE',
    'LOCK',
    'LONG',
    'MAXEXTENTS',
    'MINUS',
    'MLSLABEL',
    'MODE',
    'MODIFY',
    'NOAUDIT',
    'NOCOMPRESS',
    'NOT',
    'NOWAIT',
    'NULL',
    'NUMBER',
    'OF',
    'OFFLINE',
    'ON',
    'ONLINE',
    'OPTION',
    'OR',
    'ORDER',
    'PCTFREE',
    'PRIOR',
    'PRIVILEGES',
    'PUBLIC',
    'RAW',
    'RENAME',
    'RESOURCE',
    'REVOKE',
    'ROW',
    'ROWID',
    'ROWNUM',
    'ROWS',
    'SELECT',
    'SESSION',
    'SET',
    'SHARE',
    'SIZE',
    'SMALLINT',
    'START',
    'SUCCESSFUL',
    'SYNONYM',
    'SYSDATE',
    'TABLE',
    'THEN',
    'TO',
    'TRIGGER',
    'UID',
    'UNION',
    'UNIQUE',
    'UPDATE',
    'USER',
    'VALIDATE',
    'VALUES',
    'VARCHAR',
    'VARCHAR2',
    'VIEW',
    'WHENEVER',
    'WHERE',
    'WITH',
))

SQLITE = set((
    'ABORT',
    'ACTION',
    'ADD',
    'AFTER',
    'ALL',
    'ALTER',
    'ANALYZE',
    'AND',
    'AS',
    'ASC',
    'ATTACH',
    'AUTOINCREMENT',
    'BEFORE',
    'BEGIN',
    'BETWEEN',
    'BY',
    'CASCADE',
    'CASE',
    'CAST',
    'CHECK',
    'COLLATE',
    'COLUMN',
    'COMMIT',
    'CONFLICT',
    'CONSTRAINT',
    'CREATE',
    'CROSS',
    'CURRENT_DATE',
    'CURRENT_TIME',
    'CURRENT_TIMESTAMP',
    'DATABASE',
    'DEFAULT',
    'DEFERRABLE',
    'DEFERRED',
    'DELETE',
    'DESC',
    'DETACH',
    'DISTINCT',
    'DROP',
    'EACH',
    'ELSE',
    'END',
    'ESCAPE',
    'EXCEPT',
    'EXCLUSIVE',
    'EXISTS',
    'EXPLAIN',
    'FAIL',
    'FOR',
    'FOREIGN',
    'FROM',
    'FULL',
    'GLOB',
    'GROUP',
    'HAVING',
    'IF',
    'IGNORE',
    'IMMEDIATE',
    'IN',
    'INDEX',
    'INDEXED',
    'INITIALLY',
    'INNER',
    'INSERT',
    'INSTEAD',
    'INTERSECT',
    'INTO',
    'IS',
    'ISNULL',
    'JOIN',
    'KEY',
    'LEFT',
    'LIKE',
    'LIMIT',
    'MATCH',
    'NATURAL',
    'NO',
    'NOT',
    'NOTNULL',
    'NULL',
    'OF',
    'OFFSET',
    'ON',
    'OR',
    'ORDER',
    'OUTER',
    'PLAN',
    'PRAGMA',
    'PRIMARY',
    'QUERY',
    'RAISE',
    'REFERENCES',
    'REGEXP',
    'REINDEX',
    'RELEASE',
    'RENAME',
    'REPLACE',
    'RESTRICT',
    'RIGHT',
    'ROLLBACK',
    'ROW',
    'SAVEPOINT',
    'SELECT',
    'SET',
    'TABLE',
    'TEMP',
    'TEMPORARY',
    'THEN',
    'TO',
    'TRANSACTION',
    'TRIGGER',
    'UNION',
    'UNIQUE',
    'UPDATE',
    'USING',
    'VACUUM',
    'VALUES',
    'VIEW',
    'VIRTUAL',
    'WHEN',
    'WHERE',
))

# remove from here when you add a list.
JDBCSQLITE = SQLITE
DB2 = INFORMIX = INGRES = JDBCPOSTGRESQL = COMMON

ADAPTERS = {
    'sqlite': SQLITE,
    'mysql': MYSQL,
    'postgres': POSTGRESQL,
    'postgres_nonreserved': POSTGRESQL_NONRESERVED,
    'oracle': ORACLE,
    'mssql': MSSQL,
    'mssql2': MSSQL,
    'db2': DB2,
    'informix': INFORMIX,
    'firebird': FIREBIRD,
    'firebird_embedded': FIREBIRD,
    'firebird_nonreserved': FIREBIRD_NONRESERVED,
    'ingres': INGRES,
    'ingresu': INGRES,
    'jdbc:sqlite': JDBCSQLITE,
    'jdbc:postgres': JDBCPOSTGRESQL,
    'common': COMMON,
}

ADAPTERS['all'] = reduce(lambda a,b:a.union(b),(x for x in ADAPTERS.values()))

