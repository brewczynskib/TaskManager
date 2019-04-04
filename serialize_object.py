def convert_to_dict(obj):
	'''convert object to dict, inspired by Rodgers Ouma Mc'Alila'''

	obj_dict = {

	"__class__": obj.__class__.__name__,
	"__module__": obj.__module__

	}
	obj_dict.update(obj.__dict__)
	return obj_dict
