def create_json_response(description, data):
	return {
		"status_code":200,
		"description": description,
		"data": data
	}