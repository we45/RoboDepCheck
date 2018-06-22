## RoboDepCheck
 Robot Framework Library for OWASP Dependency Check SCA Tool


**Supports Python 2.7.x for now**

### Install Instructions
* You need docker to run this program
* Pull the OWASP Dependency Check docker image: `docker pull owasp/dependency-check`


### Keywords

`run depcheck against source`

`| run depcheck against source  | source code path  | results path  | nvd db path`

* source code path: where your source code is located currently
* results path: where your results will be stored. An `.html` file , `.xml` file and  `.json` files are generated as outputs
* nvd db path: where nvd db will be stored