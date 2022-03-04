from random import *


### How it works ###
# Sem 1: 33% of total clubs audited
#   a. initialize clubs
#   b. intialize percentage
#   c. calculate number of clubs being audited
#   d. choose clubs to audit
#   e. find the auditedClubs
#   f. add audited clubs to list of lists of clubs audited each semester
#   g. calculate clubChange
#   h. calculate eligible clubs
# Sem 2: 33% of total clubs audited not audited last semester
#   a. calculate number of clubs being audited
#   b. choose clubs to audit from eligibleClubs
#   c. find the auditedClubs
#   d. add audited clubs to list of lists of clubs audited each semester
#   e. calculate clubChange
#   f. calculate eligible clubs
# Sem 3: Any un-Audited clubs are audited
#   a. add eligibleClubs to list of audited clubs (since we are auditing them all
#   b. calculate clubChange
#   c. calculate eligible clubs
#       i. add clubs audited in sem 1 + 2
#       ii. add clubs that haven't been audited yet
# Sem 4: 33% of clubs Audited in sem 1 + sem 2 combined
#   a. calculate number or clubs being audited
#   b. choose clubs to audit from eligibleClubs
#       i. unaudited clubs are automatically audited then clubs from sem 1 + sem 2 are chosen
#   c. find the audited clubs
#   d. add audited clubs to list of lists of clubs audited each semester
#   e. calculate clubChange
#   f. calculate eligible clubs
#       i. add clubs from sem 2 + sem 3
#       ii. any clubs from sem 1 that were not audited are automatically going to be
# sem 5: 33% clubs comprised of sem 2 + sem 3 + un-Audited clubs from sem 1
#   a. calculate number or clubs being audited
#   b. choose clubs to audit from eligibleClubs
#       i. unaudited clubs from sem 1 are automatically audited then clubs from sem 2 + sem 3 + any added clubs are chosen
#   c. find the audited clubs
#   d. add audited clubs to list of lists of clubs audited each semester
#   e. calculate clubChange
#   f. calculate eligible clubs
#       i. add unaudited clubs from sem 2 + sem 3 + clubChanges
# Sem 6: Any un-Audited clubs are audited
# sem 7: 33% of clubs Audited in sem 4 + sem 5 combined
# sem 8: 33% clubs comprised of sem 5 + sem 6 + un-Audited clubs from sem 4
# sem 9: Any un-Audited clubs are audited
# firstSemCycle = 4, 7
# secondSemCycle = 5, 8
# thirdSemCycle = 3, 6, 9
# special cases = 1, 2

def ranClubs(chosenClubsInd, clubs, eligibleClubs):
    # This is the function that chooses a random club from the list of eligible clubs
    # club represents the index of a club in the list of clubs in this function
    club = randint(0, len(clubs) - 1)

    if club not in chosenClubsInd and clubs[club] in eligibleClubs:
        # If the club isnt already chosen and its and eligible club, add it to the list of chosen clubs
        chosenClubsInd.append(club)
    else:
        # Otherwise, run this function, pick another club and try again until you find a club that you can add to the list
        chosenClubsInd = ranClubs(chosenClubsInd, clubs, eligibleClubs)
    return chosenClubsInd


def clubChanges(clubs, biggestClub):
    # This function calculates the Semesterly change of the number of clubs reciving funding from the senate
    clubChange = randint(-2, 2)
    # We start by picking a random number between -2 and 2
    print("Club Change: " + str(clubChange))
    if clubChange < 0:
        # If the change in clubs is less than 0
        # We run a loop while the change in clubs is less than 0,
        # then we remove the last club from the list
        # and imcrement clubChange (to terminate the loop eventually)
        while clubChange < 0:
            clubs.remove(clubs[-1])
            clubChange += 1
    else:
        # If the change is greate than 0
        # we add a new club that is a number 1 greater than the biggest club (number) in the list (so we always have unique numbers)
        # it then increments the value of the biggest club and decrements the clubChange ot end the loop
        while clubChange > 0:
            clubs.append(biggestClub + 1)
            biggestClub += 1
            clubChange -= 1
    return clubs, biggestClub


def printAudits(audits):
    num = 1
    for audit in audits:
        print("Semester " + str(num) + " audit:")
        print(*audit)
        num += 1


def firstSemCycle(audits, clubs, semester, eligibleClubs, priorityClubs, percentage, biggestClub):
    # This is the function for the first semester in the three semester audit cycle
    print("Clubs:")
    print(*clubs)

    numAudit = round(len(clubs) * percentage)  # Calculate the number of clubs being audited based on our precentage
    # ^^ (multiplies the number of clubs by our percentage and rounds it to the nearest integer) ^^
    print("Number of clubs being audited: " + str(numAudit))

    # ###############################################
    # This block of code below uses a function called "ranClubs" (its above and so are the
    # comments on how it works) the function basically picks a random number between 0 and
    # the total number of clubs it then adds it to a list after checking to see that the
    # number is not already in the list (a club cannot get audited twice in one semester)
    chosenClubsInd = []
    for i in range(numAudit - len(priorityClubs)):
        # This for loop also account for clubs that were not audited in the last semester and makes sure they
        # are audited this semester
        chosenClubsInd = ranClubs(chosenClubsInd, clubs, eligibleClubs)

    ##############################################
    # This block of code uses the indexes we found above to make a list of the audited clubs
    # This is where the actual auditing would take place
    auditedClubs = []
    for ind in chosenClubsInd:
        club = clubs[ind]
        auditedClubs.append(club)
    # We also add in our priority clubs (clubs that didnt get audited last semester)
    for club in priorityClubs:
        auditedClubs.append(club)

    audits.append(auditedClubs)

    print("Clubs Audited Semester " + str(semester) + ":")
    print(*auditedClubs)
    printAudits(audits)

    ###################################################################################
    ##################################################################################
    # This next block of code is a lot so be ready. It basically is going to prepare our
    # eligible clubs and priority clubs for the next semester.
    # For this firstSemCycle priority clubs are clubs from 3 semesters ago that have not
    # been audited in the past 2 semesters
    # eligible clubs are clubs from 1 semesters ago and 2 semesters ago that have already been audited
    oldClubs = clubs
    clubs, biggestClub = clubChanges(clubs, biggestClub)  # calculate the club change so if we gain clubs they are
    # automatically priority clubs
    eligibleClubs = []
    priorityClubs = []
    for club in clubs:
        if club not in oldClubs:
            eligibleClubs.append(club)
    for club in audits[semester - 3]:
        if club not in auditedClubs:
            eligibleClubs.append(club)
    for club in audits[semester - 2]:
        eligibleClubs.append(club)
    for club in audits[semester - 4]:
        if club not in auditedClubs:
            priorityClubs.append(club)

    print("End of Semester " + str(semester) + " eligible clubs")
    print(*eligibleClubs)
    print("End of Semester " + str(semester) + " priority clubs")
    print(*priorityClubs)
    return clubs, eligibleClubs, priorityClubs, biggestClub


def secondSemCycle(audits, clubs, semester, eligibleClubs, priorityClubs, percentage, biggestClub):
    # This is the function for the second semester in the three semester audit cycle
    print("Clubs:")
    print(*clubs)
    # sem 5: 33% clubs comprised of currsem - 3 + currSem-2 + un-Audited clubs from currSem - 4
    # a. calculate number or clubs being audited
    # Calculate the number of clubs being audited
    numAudit = round(len(clubs) * percentage)

    print("Number of clubs being audited: " + str(numAudit))
    # b. choose clubs to audit from eligibleClubs

    # ###############################################
    # This block of code below uses a function called "ranClubs" (its above and so are the
    # comments on how it works) the function basically picks a random number between 0 and
    # the total number of clubs it then adds it to a list after checking to see that the
    # number is not already in the list (a club cannot get audited twice in one semester)
    #
    chosenClubsInd = []
    for i in range(numAudit - len(priorityClubs)):
        chosenClubsInd = ranClubs(chosenClubsInd, clubs, eligibleClubs)
        # i. unaudited clubs from currSem - 4 are automatically audited then clubs from currsem - 3 + currSem-2 + any added clubs are chosen
        # c. find the audited clubs

    ##############################################
    # This block of code uses the indexes we found above to make a list of the audited clubs
    # This is where the actual auditing would take place
    auditedClubs = []
    for ind in chosenClubsInd:
        club = clubs[ind]
        auditedClubs.append(club)
    for club in priorityClubs:
        auditedClubs.append(club)

    # We then add this semesters audit to our list fo audits
    audits.append(auditedClubs)

    print("Clubs Audited Semester " + str(semester) + ":")
    print(*auditedClubs)
    printAudits(audits)

    ###################################################################################
    ##################################################################################
    # This next block of code is a lot so be ready. It basically is going to prepare our
    # eligible clubs and priority clubs for the next semester.
    # For this secondSemCycle, any clubs that were audited 3 semesters ago are automatically added to the priority Clubs
    # Otherwise any clubs that was added is eligible and so are clubs from 2 semesters ago and one semester ago
    oldClubs = clubs
    clubs, biggestClub = clubChanges(clubs, biggestClub)
    # f. calculate eligible clubs
    # i. add unaudited clubs from currsem - 3 + currSem-2 + clubChanges
    eligibleClubs = []
    priorityClubs = []
    for club in clubs:
        if club not in oldClubs:
            eligibleClubs.append(club)
    for club in audits[semester - 3]:
        eligibleClubs.append(club)
    for club in audits[semester - 4]:
        if club not in auditedClubs:
            priorityClubs.append(club)

    print("End of Semester " + str(semester) + " eligible clubs")
    print(*eligibleClubs)
    print("End of Semester " + str(semester) + " priority clubs")
    print(*priorityClubs)
    return clubs, eligibleClubs, priorityClubs, biggestClub


def thirdSemCycle(audits, eligibleClubs, priorityClubs, clubs, semester, biggestClub):
    # this is the function for the third semestrer in the three semester cycle
    print("Clubs:")
    print(*clubs)

    # First we add all of our priority clubs to our eligible clubs if we have any priority Clubs
    # then we add thast list to our list of audits. This is because the 3rd semester in the cycle is the remainder of
    # the semester where any unaudited clubs in the past two semester get audited.
    if (len(priorityClubs) != 0):
        for club in priorityClubs:
            eligibleClubs.append(club)
    audits.append(eligibleClubs)

    print("Clubs Audited Semester " + str(semester) + ":")
    print(*eligibleClubs)
    printAudits(audits)

    # Then we calculate the club change for the next semester
    clubs, biggestClub = clubChanges(clubs, biggestClub)
    # c. calculate eligible clubs
    # i. add clubs audited in currSem-2 + currSem-1
    # Now we create the list of eligible clubs by taking all of the clubs audited two semesters ago and last semester
    eligibleClubs = audits[semester - 3] + audits[semester - 2]
    # ii. add clubs that haven't been audited yet

    # Now we generate our list of priority clubs
    # In this cycle, priority clubs are clubs in our list of clubs that were not audited in this last cycle and
    # is not in the list of eligible clubs we just made
    priorityClubs = []
    for club in clubs:
        if club not in audits[semester - 1] and club not in eligibleClubs:
            priorityClubs.append(club)

    print("End of Semester " + str(semester) + " eligible clubs")
    print(*eligibleClubs)
    print("End of Semester " + str(semester) + " priority clubs")
    print(*priorityClubs)
    return clubs, eligibleClubs, priorityClubs, biggestClub


def audit(numSemesters):
    # This is the main function that actually implements the audit selection system.
    # You can specify the number of semester you want to audit when you run the program.

    semester = 1  # Represents the current semester
    block = 1  # represents a "block" in which all clubs have been audited (every three semesters)
    audits = []  # This will be out list of audits for every semester audited
    while semester <= numSemesters:
        # This is our primary loop that does the auditing
        # it runs for the number of semesters specified by the user
        print("######################################################")
        print("######################################################")
        print("Semester: " + str(semester))
        print("Cycle: " + str(block))
        # The if statement below is executed only for the first semester
        if semester == 1:
            clubs = [i for i in range(1,
                                      11)]  # creates a list with the simulated clubs each club is represented as a number between one and n-1
            # ^^ If you want to change the number of clubs being audited, change range(1, THIS NUMBER) to range(1, WHATEVER NUMBER YOU WANT + 1)
            # for example if you want to run 45 clubs, it should be: range(1, 46)
            biggestClub = clubs[-1]
            # initialize our biggest club (just the highest number) which will be used when adding in clubs later
            print("Clubs:")
            print(*clubs)
            percentage = 0.33  # Percent of clubs audited each semester
            numAudit = round(
                len(clubs) * percentage)  # Calculate the number of clubs being audited based on our precentage
            # ^^ (multiplies the number of clubs by our percentage and rounds it to the nearest integer) ^^
            print("Number of clubs being audited: " + str(numAudit))

            # ###############################################
            # This block of code below uses a function called "ranClubs" (its above and so are the
            # comments on how it works) the function basically picks a random number between 0 and
            # the total number of clubs it then adds it to a list after checking to see that the
            # number is not already in the list (a club cannot get audited twice in one semester)
            eligibleClubs = clubs
            chosenClubsInd = []
            for i in range(numAudit):
                chosenClubsInd = ranClubs(chosenClubsInd, clubs, eligibleClubs)
            # We end up with a list containing the indexes of the clubs we are going to audit
            ###############################################
            ##############################################

            ##############################################
            # This block of code uses the indexes we found above to make a list of the audited clubs
            # This is where the actual auditing would take place
            auditedClubs = []
            for ind in chosenClubsInd:
                club = clubs[ind]
                auditedClubs.append(club)
            # We then add this list that we created to another list that will contain all audits we habe done
            audits.append(auditedClubs)

            print("Clubs Audited Semester " + str(semester) + ":")
            print(*auditedClubs)
            printAudits(audits)

            ######################################################################################
            # Here we calculate the change in clubs for the semester using the clubChanges function
            # It is explained above in detail, but it basically picks a number between -2 and 2 and
            # adds or removes that many clubs from our list of Clubs
            # This is to account for some variability in the amount of clubs reciving funding from
            # the Student Senate in any given semester
            clubs, biggestClub = clubChanges(clubs, biggestClub)

            ######################################################################################
            # We now figure out which clubs are eligible to be audited for the next semester
            # For the first semester we do this by going through our list of clubs and adding
            # the ones that we didn't audit this semester to the lit
            eligibleClubs = []
            for club in clubs:
                if club not in auditedClubs:
                    eligibleClubs.append(club)

            print("Semester " + str(semester) + " Clubs eligible to be audited:")
            print(*eligibleClubs)
            # increment the semester since we are done with semester 1
            semester += 1
        # This "if" statement is executed only for the second semester
        elif semester == 2:
            print("Clubs:")
            print(*clubs)

            # Like we did in the first semester (and you will be seeing the line below a lot)
            # we are now calculating the number of clubs to audit for the second Semester
            numAudit = round(len(clubs) * percentage)

            print("Number of clubs being audited: " + str(numAudit))

            # ###############################################
            # This block of code below uses a function called "ranClubs" (its above and so are the
            # comments on how it works) the function basically picks a random number between 0 and
            # the total number of clubs it then adds it to a list after checking to see that the
            # number is not already in the list (a club cannot get audited twice in one semester)
            # We also check to make sure that the club is eligible to be audited
            chosenClubsInd = []
            for i in range(numAudit):
                chosenClubsInd = ranClubs(chosenClubsInd, clubs, eligibleClubs)
            # We end up with a list containing the indexes of the clubs we are going to audit
            ###############################################
            ##############################################

            ##############################################
            # This block of code uses the indexes we found above to make a list of the audited clubs
            # This is where the actual auditing would take place
            auditedClubs = []
            for ind in chosenClubsInd:
                auditedClubs.append(clubs[ind])

            print("Clubs Audited Semester " + str(semester) + ":")
            print(*auditedClubs)
            audits.append(auditedClubs)
            printAudits(audits)

            ######################################################################################
            # Here we calculate the change in clubs for the semester using the clubChanges function
            # It is explained above in detail, but it basically picks a number between -2 and 2 and
            # adds or removes that many clubs from our list of Clubs
            # This is to account for some variability in the amount of clubs reciving funding from
            # the Student Senate in any given semester
            clubs, biggestClub = clubChanges(clubs, biggestClub)

            ######################################################################################
            # We now figure out which clubs are eligible to be audited for the next semester
            # For the first semester we do this by going through our list of clubs and adding
            # the ones that we didn't audit this semester to the lit
            eligibleClubs = []
            priorityClubs = []
            for club in clubs:
                if club not in auditedClubs and club not in audits[0]:
                    eligibleClubs.append(club)

            print("Semester " + str(semester) + " Clubs eligible to be audited:")
            print(*eligibleClubs)
            # increment the semester since we are done with semester 1
            semester += 1
        else:
            if semester % 3 == 0:
                # If the semester is cleanly divisible by 3 (every 3rd semester) then we run the thirdSemCycle function
                # (explained above)
                clubs, eligibleClubs, priorityClubs, biggestClub = thirdSemCycle(audits, eligibleClubs, priorityClubs, clubs,
                                                                    semester, biggestClub)
                block += 1
            elif (semester - 1) % 3 == 0:
                # Otherwise if the semester - 1 is cleanly divisible by 3 (For example 4) then we run the firstSemCycle
                # function (the first semester in the three semester cycle)
                # (explained above)
                clubs, eligibleClubs, priorityClubs, biggestClub = firstSemCycle(audits, clubs, semester, eligibleClubs,
                                                                    priorityClubs, percentage, biggestClub)
            elif (semester - 2) % 3 == 0:
                # Otherwise if the semester - 2 is cleanly divisible by 3 (For example 5) then we run the secondSemCycle
                # function (the second semester in the three semester cycle)
                # (explained above)
                clubs, eligibleClubs, priorityClubs, biggestClub = secondSemCycle(audits, clubs, semester, eligibleClubs,
                                                                     priorityClubs, percentage, biggestClub)
            semester += 1
        print("\n")


audit(9)
