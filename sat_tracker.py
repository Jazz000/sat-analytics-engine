# SAT Analytics Engine: A tool to optimize study efficiency
def run_diagnostic():
    print("--- Digital SAT Performance Tracker ---")
    
    # Categories based on Digital SAT domains
    data = {
        "Standard English Punctuation": 0,
        "Words in Context": 0,
        "Algebra & Linear Equations": 0,
        "Coordinate Geometry": 0,
        "Cross-Text Connections": 0,
        "Command of Evidence": 0,
        "Central Ideas": 0,
        "Inferences": 0,
        "Grammer": 0,
        "Transitions": 0,
        "Trigonometry": 0,
        "Data Analysis": 0,
    }

    while True:
        print("\nAvailable Categories:", ", ".join(data.keys()))
        topic = input("Enter category of error (or type 'done'): ").strip()
        
        if topic.lower() == 'done':
            break
        
        if topic in data:
            data[topic] += 1
        else:
            print("Please enter a valid category from the list.")

    total_errors = sum(data.values())
    
    if total_errors > 0:
        print("\n--- PRIORITY ANALYSIS ---")
        # Sort by most frequent errors to show what to study first
        for topic, count in sorted(data.items(), key=lambda item: item[1], reverse=True):
            percentage = (count / total_errors) * 100
            print(f"{topic}: {count} errors ({percentage:.1f}%)")
    else:
        print("No errors logged. Ready for the next practice test!")

if __name__ == "__main__":
    run_diagnostic()
