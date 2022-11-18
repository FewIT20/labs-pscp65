from time import process_time
from typing import Tuple
import re


def frame_ball_no(count: int) -> Tuple[int, int]:
    frame_no = count // 2 + 1
    ball_no = count % 2 + 1
    if count == 20:
        frame_no = 10
        ball_no = 3
    return frame_no, ball_no


def input_message(frame_no: int, ball_no: int, remaining_pins: int) -> int:
    while True:
        print(f'<<-- Frame {frame_no} * Ball {ball_no} -->>')
        number_of_pins = input(f'Enter between 0 to {str(remaining_pins)}: ')
        if not number_of_pins:
            number_of_pins = 'NO INPUT'
            print(number_of_pins)
        if re.findall(r'\b\d+\b', number_of_pins) \
                and (0 <= int(number_of_pins) <= remaining_pins):
            break
        print('Wrong Input. Enter number again\n')
    return int(number_of_pins)


def reset_pin(frame_no: int, ball_no: int, score: list) -> list:
    score.append(input_message(frame_no, ball_no, 10))
    return score


def throw_again(frame_no: int, ball_no: int, score: list) -> list:
    remaining_pins = 10 - score[-1]
    score.append(input_message(frame_no, ball_no, remaining_pins))
    return score


def ball_not_thrown(score: list) -> list:
    score.append(False)
    return score


def pin_control_and_scoring(count: int, score: list, f_score: list) -> None:
    frame_no, ball_no = frame_ball_no(count)
    if frame_no < 10:
        if ball_no != 1 and (score[-1] == 10):
            ball_not_thrown(score)
        elif ball_no == 2:
            throw_again(frame_no, ball_no, score)
        else:
            reset_pin(frame_no, ball_no, score)
    else:
        if ball_no == 1:
            reset_pin(frame_no, ball_no, score)
        elif ball_no == 2:
            if score[-1] == 10:
                reset_pin(frame_no, ball_no, score)
            else:
                throw_again(frame_no, ball_no, score)
        else:
            if sum(score[-2:]) < 10:
                ball_not_thrown(score)
            elif score[-1] == 10 or sum(score[-2:]) == 10:
                reset_pin(frame_no, ball_no, score)
            else:
                throw_again(frame_no, ball_no, score)
    display_scoreboard(frame_no, ball_no, score, f_score)


def frame_score_calculator(idx: int, score: list, f_score: list,
                           bonus_count: int) -> None:
    count = 0
    step = 2
    bonus = 0
    while count != bonus_count and (idx + step) < len(score):
        if score[idx + step] or type(score[idx + step]) == int:
            bonus += score[idx + step]
            count += 1
        step += 1
    if count == bonus_count:
        f_score[int(idx / 2)] = sum(score[idx:idx + 2]) + bonus


def display_scoreboard(frame_no: int, ball_no: int,
                       score: list, f_score: list) -> None:
    if (frame_no < 10 and ball_no == 2) or ball_no == 3:
        print('\nSCORE BOARD')
        line_one = '   Frame    '
        line_two = '   Result   '
        line_three = 'Frame Score '
        line_four = 'Total Score '

        for number in range(0, 10):
            line_one += '|' + str(format(number + 1, '^5d'))

        for idx in range(0, len(score), 2):
            if idx == 18:
                f_score[9] = (sum(score[-3:]))
                break
            if score[idx:idx + 2] == [10, False]:
                frame_score_calculator(idx, score, f_score, 2)
            elif sum(score[idx:idx + 2]) == 10:
                frame_score_calculator(idx, score, f_score, 1)
            else:
                frame_score_calculator(idx, score, f_score, 0)

        for idx in range(0, frame_no):
            if idx != 9:
                if score[2 * idx] == 10:
                    line_two += '|' + str(format('X', '^5s'))
                elif sum(score[2 * idx:2 * (idx + 1)]) == 10:
                    line_two += '| ' + str(score[2 * idx]) + ' / '
                else:
                    line_two += '| ' + str(score[2 * idx]) \
                                + ' ' + str(score[2 * idx + 1]) + ' '
            else:
                if score[-3] == 10:
                    line_two += '|X'
                    if score[-2] == 10:
                        line_two += ' X'
                        if score[-1] == 10:
                            line_two += ' X'
                        else:
                            line_two += ' ' + str(score[-1])
                    else:
                        line_two += ' ' + str(score[-2])
                        if sum(score[-2:]) == 10:
                            line_two += ' /'
                        else:
                            line_two += ' ' + str(score[-1]) + ''
                else:
                    line_two += '|' + str(score[-3])
                    if sum(score[-3:-1]) == 10:
                        line_two += ' /'
                        if score[-1] == 10:
                            line_two += ' X'
                        else:
                            line_two += ' ' + str(score[-1]) + ''
                    else:
                        line_two += ' ' + str(score[-2]) + '  '
            if f_score[idx] or type(f_score[idx]) == int:
                line_three += '|' + format(f_score[idx], '^5d')
                line_four += '|' + format(sum(f_score[:idx + 1]), '^5d')

        diff_two = (len(line_one) - len(line_two)) // 6
        diff_three = (len(line_one) - len(line_three)) // 6
        print(line_one, end='|\n')
        print(line_two + '|     ' * diff_two, end='|\n')
        print(line_three + '|     ' * diff_three, end='|\n')
        print(line_four + '|     ' * diff_three, end='|\n\n')


start = process_time()
score_board = list()
frame_score = [False for _ in range(10)]
print('<<--    GAME START    -->>')
for ball_count in range(21):
    pin_control_and_scoring(count=ball_count,
                            score=score_board, f_score=frame_score)
print('<<--    END OF GAME   -->>')
print(f'Elapsed time: {(process_time() - start) * 1000:.5f}ms.')