import json

# Load the JSON data once
with open("q-vercel-python.json", "r") as f:
    students = json.load(f)

# Make a quick lookup dict: name → marks
marks_dict = {student["name"]: student["marks"] for student in students}

def handler(request):
    names = request.args.getlist("name")
    results = [marks_dict.get(name, None) for name in names]

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps({ "marks": results })
    }
