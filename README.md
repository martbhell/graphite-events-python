graphite_annotation.py
------------
A python script to send annotations to graphite's event store

Requirements
------------

python2

pip install urllib[secure]

We verify certificates, this depends on the urllib3[secure] libraries.

Not tested with python3

Usage
------------
<pre>
python graphite_annotation.py --what "Title" --tag "tag" --data "D" --url https://example.com
</pre>
