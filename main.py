from quests import cards
from random import randint

def main():
    slots = (list(cards.items()), [], [])
    box_chance_mul = [4, 2, 1]
    try:
        while True:
            wts = [len(i) * box_chance_mul[idx] for idx, i in enumerate(slots)]
            f = randint(1, sum(wts)) - 1
            box_idx = 0
            a = 0
            n = 0
            for idx, i in enumerate(wts):
                a += i
                if f < a:
                    box_idx = idx
                    n = f - a + i
                    break
            box = slots[box_idx]
            q, a = box.pop(n // box_chance_mul[box_idx])
            print(chr(27) + "[2J")
            print(q)
            print("-" * 4)
            ans = input("Answer: ")
            print(f"The answer was: {a}")
            print("=" * 5)
            o = input("Were you correct? (Y/n/exit): ")
            if not o or o[0].lower() == "y":
                box_idx = min(box_idx + 1, len(slots) - 1)
            elif o[0].lower() == "n":
                box_idx = max(box_idx - 1, 0)
            else:
                break
            slots[box_idx].append((q, a))
            if len(cards) == len(slots[-1]):
                print(f"You have memorized all {len(cards)} cards")
                break
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        calculate_performance(slots)

def calculate_performance(slots):
    total_cards = sum(len(slot) for slot in slots)
    total_correct = len(slots[-1])
    accuracy = (total_correct / total_cards) * 100
    print("\n\nPerformance Metrics:")
    print(f"Total Cards: {total_cards}")
    print(f"Total Correct: {total_correct}")
    print(f"Accuracy: {accuracy:.2f}%")

if __name__ == "__main__":
    main()
