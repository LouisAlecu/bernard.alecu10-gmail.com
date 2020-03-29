export SP_DB_HOST=localhost
export SP_DB_NAME=sp
export SP_DB_USER=postgres
export SP_DB_PORT=5433
export SP_DB_PASS=''
export SP_FILE_DB=$(pwd)/sp_file_db

echo $SP_DB_HOST
pushd sp_py
python ./sp_py/pull.py
python ./sp_py/push.py
