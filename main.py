import answers
from crates import move_stacks
from filesystem import small_directories_sum, smallest_dir_to_delete
from find_marker import find_marker_index
from overlap import total_overlap_count, partial_overlap_count
from richest_elf import richest_elf
from rps import score_from_strategy
from rps_2 import score_from_strategy as score_from_strategy_2
from rucksack import odd_item_sum
from rucksack_badge import badges_sum
from three_rich_elves import richest_elves


def check_answers():
    """
    Checks all the answers. Defines input files.
    """
    print("Dec 1:")
    print(
        f"Part I: {'Correct' if richest_elf('data/elf_food.txt') == answers.a_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if richest_elves('data/elf_food.txt') == answers.a_b else 'Incorrect'}"
    )
    print("Dec 2:")
    print(
        f"Part I: {'Correct' if score_from_strategy('data/elf_strategy.txt') == answers.b_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if score_from_strategy_2('data/elf_strategy.txt') == answers.b_b else 'incorrect'}"
    )
    print("Dec 3:")
    print(
        f"Part I: {'Correct' if odd_item_sum('data/knapsacks.txt') == answers.c_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if badges_sum('data/knapsacks.txt') == answers.c_b else 'Incorrect'}"
    )
    print("Dec 4:")
    print(
        f"Part I: {'Correct' if total_overlap_count('data/sections.txt') == answers.d_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if partial_overlap_count('data/sections.txt') == answers.d_b else 'Incorrect'}"
    )
    print("Dec 5:")
    print(
        f"Part I: {'Correct' if move_stacks('data/crates.txt', False) == answers.e_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if move_stacks('data/crates.txt', True) == answers.e_b else 'Incorrect'}"
    )
    print("Dec 6:")
    print(
        f"Part I: {'Correct' if find_marker_index('data/communique.txt', 4) == answers.f_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if find_marker_index('data/communique.txt', 14) == answers.f_b else 'Incorrect'}"
    )
    print("Dec 7:")
    print(
        f"Part I: {'Correct' if small_directories_sum('data/console_log.txt') == answers.g_a else 'Incorrect'}"
    )
    print(
        f"Part II: {'Correct' if smallest_dir_to_delete('data/console_log.txt') == answers.g_b else 'Incorrect'}"
    )


if __name__ == "__main__":
    check_answers()
