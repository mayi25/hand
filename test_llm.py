""" The main app for the robot hand """
import time
import llm

def main():
    """
    Main function to record audio, transcribe it, and then query the llm.
    """
    answer = ""
    correct_answer = 0
    wrong_answer = 0
    try:
        with open("questions.txt", 'r') as file:
            for line in file:
                processed_line = line.strip()
                if len(processed_line) == 1:
                    if answer.upper() == processed_line.upper()[:1]:
                        correct_answer += 1
                    else:
                        wrong_answer += 1
                else:
                    response = llm.query_ollama('Try to answer the question in one letter. ' + processed_line)
                    answer = response.strip()
                    print(f"{processed_line}\n{answer}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    print(f"correct:{correct_answer}, mistake: {wrong_answer}")
main()
