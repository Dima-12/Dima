import os.path

from storage.lib_file import Libfile
import os

library = Libfile(config= {
  "file" : os.path.abspath(os.curdir) + "/storage/lib.json"
})
