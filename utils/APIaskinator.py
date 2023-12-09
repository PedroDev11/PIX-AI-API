import asyncio

from akinator import (
    CantGoBackAnyFurther,
    InvalidAnswer,
    AsyncAkinator,
    Answer,
    Theme,
    Language
)

async def test():
    # create akinator instance
    aki = AsyncAkinator(
        language=Language.Spanish,
        child_mode=True,
        theme=Theme.from_str('characters'),
    )

    # start the game, and get the first question
    first_question = await aki.start_game()
    # recieve console input for first question
    answer = input(f'{first_question}: ')

    # keep asking and receiving answers while akinator's progression is <=80
    while aki.progression <= 80:
        if answer == 'atras':
            # go back a question if response is "back"
            try:
                await aki.back()
                print('went back 1 question')
                print('Regresando una pregunta atrás')
            except CantGoBackAnyFurther:
                print('No se puede retroceder más!')
        else:
            try:
                # parse to an answer enum variant
                # Map user answers to valid answers in Spanish
                answer_mapping = {
                    'si': Answer.Yes,
                    'no': Answer.No,
                    'no se': Answer.Idk,
                    'probablemente': Answer.Probably,
                    'probablemente no': Answer.ProbablyNot,
                }
                answer = answer_mapping.get(answer.lower(), None)

                if answer is None:
                    raise InvalidAnswer("Respuesta inválida")

            except InvalidAnswer:
                print('Respuesta inválida')
            else:
                # answer current question
                await aki.answer(answer)

        # receiving console input for next question
        answer = input(f'{aki.question}: ')

    # tell akinator to end the game and make its guess
    first_guess = await aki.win()

    if first_guess:
        # print out its first guess's details
        print('Nombre:', first_guess.name)
        print('Descripción:', first_guess.description)
        print('Imagen:', first_guess.absolute_picture_path)
        
if __name__ == '__main__':
    asyncio.run(test())
