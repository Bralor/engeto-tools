## Springhawk

---

This project serves for cleaning the repository that have all needed files
for academy(xml, images, exercises).

### Installation 

---

Clone the repository:
```
git clone https://github.com/Bralor/engeto-tools.git
```

Go to the root folder:
```
cd engeto-tools
```

Create a virtual enviroment:
```
python -m venv env
```

Activate the enviroment:
```
source env/bin/activate   # unix-based
env\Scripts\activate.bat  # windows
```

Install the package itself:
```
pip install .
```

### Usage

---

Updating the description of the tasks:
```
>>> import task_manager.processor as tp
>>> #task_desc_processor
>>> #tp("<engeto_repo>", "<task_package>", "<xml_source_file>")
>>> tp(
...     "../python-uvod-do-programovani",
...     "../engeto_tasks", 
...     "course_python-uvod-do-programovani.xml"
... )
```

Updating the elements `exercise` and their attribute values:
```
>>> import task_manager.processor as tp
>>> # task_attr_processor
>>> tp.task_attr_processor(
...    "../python-uvod-do-programovani",
...    "../output_xml.xml"
... )
```

Updating the content of the exercises in the folder `exercises`:
```
>>> import task_manager.processor as tp
>>> # task_content_processor
>>> tp.task_content_processor(
...    "../python-uvod-do-programovani",
...    "lesson01",
... )
```

### Development

---

to-do
