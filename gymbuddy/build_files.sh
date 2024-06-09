echo "BUILD START"
python 3.12.3 -m pip install -r requirements.txt
python 3.12.3 manage.py collectstatic --noinput --clear
echo "BUILD END"