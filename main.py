from lessons.third_lesson import thirdLesson, run
from lessons.lesson_6 import lessonSix
from excersizes.api_excersize_2 import runIt
from lessons.lesson_7 import run7
from lessons.lesson_8 import run8
from lessons.lesson_9 import run9
from lessons.lesson_10 import run10
from projects.crontab_tool.crontab_tool import runCronTab


def main():
    print(
        "-------------------------------------------- Excersize --------------------------------------------------------------" + "\n\n")

    # list_tuple_set()
    # dictionary()
    # secondLesson()
    # thirdLesson()
    # run()
    # lessonSix()
    # runIt()
    # run7()
    # run8()
    # run9()
    # run10()
    runCronTab()
    print("\n\n" +
          "-------------------------------------------- This is the end ---------------------------------------------------------")


if __name__ == '__main__':
    main();
