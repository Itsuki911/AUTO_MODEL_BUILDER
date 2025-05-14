import random

def generate_training_data(task_requirements):
    task = task_requirements.get('task', 'default task')
    labels = task_requirements.get('labels', ['label1', 'label2'])
    data_format = task_requirements.get('data_format', 'text')
    if not labels or not isinstance(labels, list):
        raise ValueError("Labels must be a non-empty list.")
    training_data = []
    for i in range(100):
        if data_format == 'text':
            sample_input = f"Sample text input {i} for {task}"
        elif data_format == 'numeric':
            sample_input = random.uniform(0, 100)
        else:
            sample_input = f"Unsupported data format: {data_format}"
        sample = {'input': sample_input, 'label': random.choice(labels)}
        training_data.append(sample)
    return training_data