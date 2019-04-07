def convert_to_dict(obj):
	'''convert object to dict, inspired by Rodgers Ouma Mc'Alila'''

	obj_dict = {

	"__class__": obj.__class__.__name__,
	"__module__": obj.__module__

	}
	obj_dict.update(obj.__dict__)
	return obj_dict


def object_to_dict(my_dict):
	'''convert our dict to object'''

	if "__class__" in my_dict:
		class_name = my_dict.pop("__class__")
		module_name = my_dict.pop("__module__")
		module = __import__(module_name)
		class_ = getattr(module.client, class_name)
		obj = class_(**my_dict)
	else: pass


