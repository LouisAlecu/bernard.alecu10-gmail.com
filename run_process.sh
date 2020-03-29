export SP_DB_HOST=localhost
export SP_DB_NAME=sp
export SP_DB_USER=postgres
export SP_DB_PORT=5433
export SP_DB_PASS=''
export SP_FILE_DB=$(pwd)/sp_file_db
export PYTHONPATH="${PYTHONPATH}:$(pwd)/sp_py/sp_py/"

pushd sp_py
python3 ./sp_py/pull.py
python3 ./sp_py/push.py
