## Springhawk

---

This project serves for cleaning the repository that have all needed files
for academy(xml, images, exercises).


### Installation 

---

Clone the repositories:
```
git clone https://github.com/Bralor/engeto-tools.git
git clone https://github.com/Bralor/engeto_tasks.git
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
>>> # Usage: tp.task_desc_processor("<engeto_repo>", "<tasks_package>")
>>> tp(
...     "../python-uvod-do-programovani",
...     "../engeto_tasks", 
... )
```

Updating the elements `exercise` and their attribute values:
```
>>> import task_manager.processor as tp
>>> # Usage: tp.task_attr_processor("<file_with_modified_descriptions.xml>")
>>> tp.task_attr_processor(
...    "../output_desc.xml"
... )
```

Updating the content of the exercises in the folder `exercises`:
```
>>> import task_manager.processor as tp
>>> # Usage: tp.task_content_processor("<engeto_repo>", "<lesson_number>")
>>> tp.task_content_processor(
...    "../python-uvod-do-programovani",
...    "lesson01",
... )
```

### Development

---

to-do
