# Global scope

# level_1 paragragh and its answers
paragraph_level_1 = 'I have a ___1___ that one day this ___2___ will rise up, live up to the ___3___ meaning of its creed: "We hold these truths to be self-evident; that all men are created ___4___."'
blanks_level_1 = ['___1___','___2___','___3___','___4___']
answer_level_1 = ['dream','nation','true','equal']

# level_2 paragragh and its answers
paragraph_level_2 = 'I have a ___1___ that one day this ___2___ will rise up, live up to the ___3___ meaning of its creed: "We hold these truths to be self-evident; that all men are created ___4___." I have a ___5___ that one day on the red hills of ___6___ the sons of former slaves and the sons of former slave-owners will be able to sit down together at the table of ___7___.'
blanks_level_2 = ['___1___','___2___','___3___','___4___','___5___','___6___','___7___']
answer_level_2 = ['dream','nation','true','equal','dream','Georgia','brotherhood']

# level_3 paragragh and its answers
paragraph_level_3 = 'I have a ___1___ that one day this ___2___ will rise up, live up to the ___3___ meaning of its creed: "We hold these truths to be self-evident; that all men are created ___4___."I have a ___5___ that one day on the red hills of ___6___ the sons of former slaves and the sons of former slave-owners will be able to sit down together at the table of ___7___. I have a ___8___ that one day even the state of ___9___, a state sweltering with the heat of ___10___, sweltering with the heat of ___11___, will be transformed into an oasis of ___12___ and justice.'
blanks_level_3 = ['___1___','___2___','___3___','___4___','___5___','___6___','___7___','___8___','___9___','___10___','___11___','___12___']
answer_level_3 = ['dream','nation','true','equal','dream','Georgia','brotherhood','dream','Mississippi','injustice','oppression','freedom']

SMALL_MULTIPLIER = 10
MEDIUM_MULTIPLIER = 20
LARGE_MULTIPLIER = 21

# Main body
def level_selection():
    '''Enable user to choose quiz level.
       If the input is not the same as explanation, stay and show the re-input prompt'''
    input_level = raw_input('\nSelect the level: [level 1, level 2 or level 3]'+' ')
    if input_level == 'level 1':
        para,blanks,answer=paragraph_level_1,blanks_level_1,answer_level_1
    elif input_level == 'level 2':
        para,blanks,answer=paragraph_level_2,blanks_level_2,answer_level_2
    elif input_level == 'level 3':
        para,blanks,answer=paragraph_level_3,blanks_level_3,answer_level_3
    else:
        print '\n'+'#'*SMALL_MULTIPLIER+' '+'Incorrect. Use the format of "level *"'+' '+'#'*SMALL_MULTIPLIER
        return level_selection()
    return para,blanks,answer

def word_in_pos(word, blanks):
    '''find out the element on blank position same with the element in this blank.
        input: 
              word: each element in paragraph
              blanks: blanks_level_# list
        output:
              blank: element with same part in blanks_level_# list's element.
        (i.e. if the blank element is "___1___," this funtion returns "___1___")'''
    for blank in blanks:
        if blank in word:
            return blank
    return None

def word_in_pos_with_punctuation(word, blanks):
    '''find out the element on blank position without modification.
        input: 
              word: each element in paragraph
              blanks: blanks_level_# list
        output:
              word: element same with blanks_level_# list's element.
    (i.e. if the blank element is "___1___," this funtion returns "___1___,")'''
    for blank in blanks:
        if blank in word:
            return word
    return None

def check(word,para,blanks,answer):
    '''check whether the user_input is same with correct answer.
       If correct, then overwrite the blank, and go to next blank;
       If it is not correct, stay and redo the check at current blank position.
       input: 
             word: each element in paragraph
             para: paragraph_level_#
             blanks: blanks_level_# list
             answer: answer_level_# list
       output: 
             para: paragraph_level_# with filled in words.'''
    replacement = word_in_pos(word,blanks)
    replacement_with_puntuation = word_in_pos_with_punctuation(word,blanks)
    if replacement != None:
        user_input = raw_input("Please fill in " + replacement+' ')
        num_in_answer_list = blanks.index(replacement)
        correct_answer = answer[num_in_answer_list]
        if user_input == correct_answer:
            blank_position = para.index(replacement_with_puntuation)
            para[blank_position] = para[blank_position].replace(replacement,user_input)
            print ' '.join(para)+'\n'
        else:
            print '\nYour answer is not correct, try again!\n\n'+' '.join(para)+'\n'
            return check(word,para,blanks,answer)

def play_game():
    '''play the game.
       First show the level selection interface;
       Then after level selection, the paragraph with blanks is shown based on the level;
       Input the word;
       Game over if all inputs are correct'''
    para,blanks,answer = level_selection()
    para = para.split()
    print '\n'+'#'*MEDIUM_MULTIPLIER+' '+'Paragraph is shown inside the box'+' '+'#'*MEDIUM_MULTIPLIER
    print ' '.join(para)
    print '#'*(LARGE_MULTIPLIER+len('Paragraph is shown inside the box')+LARGE_MULTIPLIER)+'\n'
    for num in para:
        check(num,para,blanks,answer)
    print '/'*(MEDIUM_MULTIPLIER+len('Congratulation, you made it!'))
    print '/'*SMALL_MULTIPLIER+'Congratulation, you made it!'+'/'*SMALL_MULTIPLIER
    print '/'*(MEDIUM_MULTIPLIER+len('Congratulation, you made it!'))+'\n'
    return para

play_game()






