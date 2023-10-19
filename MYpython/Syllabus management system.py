
#project:
sub=['Physics','Biology','Chemistry','English','Maths','Social science']    
print()
i=input("Enter 'Subjects' to get name of all subjects : ")
print()
if i=='subjects'.lower():
    print('Subjects are : ')
    print('-------------')
    print()
    for c in range(len(sub)) :
        print(f"{c+1}.{sub[c]}")    
        print()
    print()
    i2=input("Enter subject name to see chapters : ")
    print()
    if i2=='physics':
        phy=['light-Reflection and Refraction','The Human Eye and the colorful world','Electricity','Magnetic Effects of Electric Current','Source of Energy']
        print('Chapters of Physics')
        print('--------------------')
        print()
        for k in range(len(phy)):
            print(f'{k+1}.{phy[k]}')
            print()
    elif i2=='Biology'.lower():
        bio=['Life Procesess','Controle and Coordination','How do Organisms Reproduce?','Heredity and Evolution','Environment','Management of Natural Resources']
        print('Chapters of Biology')
        print('--------------------')
        print()
        for k in range(len(bio)):
            print(f'{k+1}.{bio[k]}')
            print()

    elif i2=='Chemistry'.lower():
        chem=['Chemical Reactions and Equations','Acids , Bases and Salts','Metals and Non-Metals','Carbon and its Compounds','Priodic Classification of Elements']
        print('Chapters of Chemistry')
        print('---------------------')
        print()
        for k in range(len(chem)):
            print(f'{k+1}.{chem[k]}')
            print()
    elif i2=='English'.lower():
        j=input('Press "F" for "Fiction" , Press "P" for "Poetry" , Press "D" for "Drama" ')
        print()
        if j=="f":
            fict=['Two Gentlemen of Verona','Mrs. Packletide’s Tiger','The Letter','A Shady Plot','Patol Babu, Film Star','Virtually True']
            print('Chapters of English_Fiction')
            print('---------------------------')
            print()
            for k in range(len(fict)):
                print(f'{k+1}.{fict[k]}')
        
        elif j=='p':
            poe=['The Frog and the Nightingale','Mirror','Not Marble, nor the Gilded Monuments','Ozymandias','The Rime of the Ancient Mariner','Snake']
            print('Chapters of English_Poetry')
            print('--------------------------')
            print()

            for k in range(len(poe)):
                print(f'{k+1}.{poe[k]}')
                print()
        elif j=='d':
            dr=['The Dear Departed','Julius Caesar']
            print('Chapters of English_Drama')
            print('-------------------------')
            print()

            for k in range(len(dr)):
                print(f'{k+1}.{dr[k]}')

    elif i2=='Maths'.lower():
         print('Chapters of Maths')
         print('------------------')
         print()
         math=['Real Numbers','Polynomials','Pair of Linear Equations in Two Variables','Quadratic Equations','Arithmetic Progressions','Triangles','Coordinate Geometry','Introduction to Trigonometry','Some Applications of Trigonometry','Circles','Constructions','Areas Related to Circles','Surface Areas And Volumes','Statistics','Probability']
         for k in range(len(math)):
             print(f'{k+1}.{math[k]}')
             print()
         print()    
         j=int(input("Enter index no. of chapter to get basic info about chapter : "))
         print()
         if j==1:
            print('Info_real_numbers')
            print('---------------------')
            rl=['Natural Numbers','Whole number','Integers','Rational Number','Irrational Number','Real Numbers']
            cont=['1,2,3,4,5','0,1,2,3,4,5','-4,-3,-2,-1,0,1,2,3,4,5… so on','number is called rational if can be expressed in the form p/q where p and q are integers (q> 0)','A number is called rational if it cannot be expressed in the form p/q where p and q are integers (q> 0)','A real number is a number that can be found on the number line']
            for m in range(len(rl)):
                print(f'{m+1}.{rl[m]} = {cont[m]}')
                print()
         elif j==2:
                print('Info_Polynomials')
                print('-----------------')
                print('A polynomial is an algebraic expression in which the variables have non-integral exponents only.Example- 3x2­­+ 4y + 2, 5x3+ 3x2 + 4x +2Degree of a Polynomial')
                pl=['Division Algorithm','Number of Zeroes','Factorisation of Polynomials',]
                vals1=['p(x) = g(x) × q(x) + r(x)','A polynomial of degree n has at most n zeros','Quadratic polynomials can be factorized by splitting the middle term. For example, consider the polynomial 2x2−5x+3']

                for vy in range(len(pl)):
                    print(f'{vy+1}.{pl[vy]} = {vals1[vy]}')
                    print()
                print()
                print('more fomulla : ')
                print('------------')

                iden=['(a+b)2 ','(a-b)2','(x+a)(x+b)','a2-b2','a3-b3','a3+b3','(a+b)3','(a-b)3']
                vals2=['a2+2ab+b2','a2−2ab+b2','x2+(a+b)x+ab','(a+b)(a−b)','(a−b)(a2+ab+b2)','(a+b)(a2−ab+b2)','a3+3a2b+3ab2+b3','a3−3a2b+3ab2−b3']
                
                for vt in range(len(iden)):
                    print(f'{vt+1}.{iden[vt]} = {vals2[vt]}')
                    print()

         elif j==3:
            print('Info_Pair of Linear Equations in Two Variables')
            print('----------------------------------------------')
            print('Linear equations in two variables are equations which can be expressed as ax + by + c = 0, where a, b and c are real numbers and both a, and b are not zero')
            print()
            print('Represented as : ax+by+c=0')
            

         elif j==4:
            print('Info_Quadratic Equations')
            print('------------------------')
            print()
            print('In algebra, a quadratic equation is any equation that can be rearranged in standard form as where x represents an unknown value, and a, b, and c represent known numbers, where a ≠ 0.') 
            print()
            print('formulla:')
            print('---------')
            print()
            form=['Standard Form of Quadratic Equation','Quadratic Formula','Discriminant ','Sum of Roots','Product of Roots']
            vals=['ax^2+ bx + c = 0, a≠0','-b ± √D⁄2a or -b ± b^2 − 4ac⁄2a','b^2 − 4ac','−b/a','c/a']
            
            for vb in range(len(form)):
                print(f'{vb+1}.{form[vb]} = {vals[vb]}')
                print()

         elif j==5:
            print('Arithmetic Progressions')
            print('-----------------------')
            print()
            print('A mathematical sequence in which the difference between two consecutive terms is always a constant and it is abbreviated as AP')
            print()
            print('formulas : ')
            print('---------')
            print()
            jl=['nth Term of an AP','Sum of N Terms of AP','Sum of AP when the Last Term is Given']
            fm=['an = a + (n − 1) × d','Sn = n/2[2a + (n − 1) × d]','S  = n/2 (first term + last term)']
            for kl in range (len(jl)):
                print(f'{kl+1}.{jl[kl]} = {fm[kl]}')
                print()
            print()
         
         elif j==6:
             print('Triangles')
             print('---------')
             print()
             print("The triangle formulas can be mathematically expressed as follows; Area of triangle, A = [(½) b × h]; where 'b' is the triangle's base and 'h' is the triangle's height. The perimeter of a triangle, P = (a + b + c), where a, b, and c are the triangle's three sides.")
             print()
             print('Theormes:')
             print('---------')
             print()
             theo=["Pythagoras Theorem","Midpoint Theorem","Remainder Theorem","Fundamental Theorem of Arithmetic","Angle Bisector Theorem","Inscribed Angle Theorem","Ceva's Theorem","Bayes' Theorem"]
             defi=['In a right-angled triangle, the square of the hypotenuse side is equal to the sum of squares of the other two sides, h=under root (a^2+b^2)','The line segment in a triangle joining the midpoint of any two sides of the triangle is said to be parallel to its third side','for any polynomial P(x) P ( x ) for any real a a , P(a) P ( a ) is exactly equal to the remainder of P(x)÷(x−a) P ( x ) ÷ ( x − a ) ','every integer greater than 1 is either a prime number or can be expressed in the form of primes.','a triangle divides the opposite side into two parts proportional to the other two sides of the triangle','The measure of the central angle is equal to twice the measure of the inscribed angle subtended by the same arc','the ratio of the products of the pairs of segments of a triangle is equal to the value of one','mathematical formula used to determine the conditional probability of the events. Actually the Bayes’ theorem describes the probability of an event based on prior knowledge of the conditions, relevant to the event']
             
             for kc in range(len(theo)):
                print(f'{kc+1}.{theo[kc]} = {defi[kc]}')
                print()
                
         elif j==7:
             print('Coordinate Geometry')
             print('-------------------')
             print("All Formulas of Coordinate Geometry,Slope Intercept Form of a Line	y = mx + c,Point-Slope Form	y − y1= m(x − x1),The slope of a Line Using Coordinates	m = Δy/Δx = (y2 − y1)/(x2 − x1)The slope of a Line Using General Equation	m = −(A/B)")
             print()
             print('formulas:')
             print('---------')
             print()
             fg=['General Form of a Line','Slope Intercept Form of a Line','Point-Slope Form','The slope of a Line Using Coordinates','The slope of a Line Using General Equation','Intercept-Intercept Form','Distance Formula','For Parallel Lines','For Perpendicular Lines','Midpoint Formula','Angle Formula','Area of a Triangle Formula','Distance from a Point to a Line','Section Formula','Section Formula']
             gh=['Ax + By + C = 0','y = mx + c','y − y1= m(x − x1)','m = Δy/Δx = (y2 − y1)/(x2 − x1)','m = −(A/B)','x/a + y/b = 1','|P1P2| = √[(x2 − x1)^2 + (y2 − y1)^2]','m1 = m2','m1m2 = -1','M (x, y) = [½(x1 + x2), ½(y1 + y2)]','tan θ = [(m1 – m2)/ 1 + m1m2]','½ |x1(y2−y3)+x2(y3–y1)+x3(y1–y2)|','d = [|Ax0 + By0 + C| / √(A^2 + B^2)]','(Internal division) : P(x, y) = [(m1x2 + m2x1)/(m1 + m2), (m1y2 + m2y1)/(m1 + m2)]','(External division) : P(x, y) = [(m1x2 – m2x1)/(m1 – m2), (m1y2 – m2y1)/(m1 – m2)]']
             for mk in range(len(fg)):
                 print(f'{mk+1}.{fg[mk]} = {gh[mk]}')
                 print()
             print()
         
         elif j==8:
             print('Introduction to Trigonometry')
             print('----------------------------')
             print('The trigonometric formulas for ratios are majorly based on the three sides of a right-angled triangle, such as the adjacent side or base, perpendicular and hypotenuse (See the above figure).  Applying Pythagoras theorem for the given right-angled triangle')
             print()
             print('Basic Trigonometric formulas')
             print('----------------------------')
             print()
             print('Property -  Mathematical value')
             print('--------    ------------------')
             print()
             
             tg1=['sin A','cos A','tan A','cot A','cosec A','sec A']
             mg1=['Perpendicular/Hypotenuse','Base/Hypotenuse','Perpendicular/Base','Base/Perpendicular','Hypotenuse/Perpendicular','Hypotenuse/Base']
             for mj in range(len(tg1)):
                 print(f'{mj+1}.{tg1[mj]} = {mg1[mj]}')
             print()
             print('Reciprocal Relation Between Trigonometric Ratios')
             print('------------------------------------------------')
             print()
             print('Identity  -  Relation')
             print()
             vf=['tan A','cot A','cosec A','sec A']
             vg=['sin A/cos A','cos A/sin A','1/sin A',' 1/cos A']
             for jm in range(len(vf)):
                 print(f'{jm+1}.{vf[jm] } = {vg[jm]}')
                 print()
             print()
             print('Trigonometric Sign Functions:')
             print('-----------------------------')
             print()
             bg=['sin (-θ)','cos (−θ)', 'tan (−θ)','cosec (−θ)', 'sec (−θ)', 'cot (−θ)']
             fc=['− sin θ','cos θ','− tan θ','− cosec θ','sec θ','− cot θ']
             for ml in range(len(bg)):
                 print(f'{ml+1}.{bg[ml]} = {fc[ml]}')
                 print()
             print()
             
             print('Trigonometric Identities:')
             print('-------------------------')
             print()
             vc=['sin2A + cos2A','tan2A + 1','cot2A + 1']
             gv=['1','sec2A','cosec2A']
             
             for mk in range(len(vc)):
                 print(f'{mk}.{vc[mk]} = {gv[mk]}')
                 print()
             print()
             
             print('Periodic Identities')
             print('--------------------')
             print()
             yh=['sin(2nπ + θ )','cos(2nπ + θ )','tan(2nπ + θ )','cot(2nπ + θ )','sec(2nπ + θ )','cosec(2nπ + θ)']
             km=['sin θ','cos θ','tan θ','cot θ','sec θ','cosec θ']
             for ki in range(len(yh)):
                 print(f'{ki+1}.{yh[ki]} = {km[ki]}')
                 print()
             print()
             
             print('Complementary Ratios:')
             print('---------------------')
             print()
             vg=['quadrant I','quadrant II','quadrant III','quadrant IV']
             vx=[['sin(π/2 − θ) = cos θ','cos(π/2 − θ) = sin θ','tan(π/2 − θ) = cot θ','cot(π/2 − θ) = tan θ','sec(π/2 − θ) = cosec θ','cosec(π/2 − θ) = sec θ'],['sin(π − θ) = sin θ','cos(π − θ) = -cos θ','tan(π − θ) = -tan θ','cot(π − θ) = – cot θ','sec(π − θ) = -sec θ','cosec(π − θ) = cosec θ'],['sin(π + θ) = – sin θ','cos(π + θ) = – cos θ','tan(π + θ) = tan θ','cot(π + θ) = cot θ','sec(π + θ) = -sec θ','cosec(π + θ) = -cosec θ'],['sin(2π − θ) = – sin θ','cos(2π − θ) = cos θ','tan(2π − θ) = – tan θ','cot(2π − θ) = – cot θ','sec(2π − θ) = sec θ','cosec(2π − θ) = -cosec θ']]
             for vf in range(len(vg)):
                print(f'{vg[vf]}')  
                print()
                print('   'f'{vx[vf]}') 
                print()
                print()
             print()
             print('Double Angle Formulas:')
             print('---------------------')
             print()
             cx=['sin 2A = 2 sin A cos A = [2 tan A /(1 + tan2A)]','cos 2A = cos2A – sin2A = 1 – 2 sin2A = 2 cos2A – 1 = [(1 – tan2A)/(1 + tan2A)]','tan 2A = (2 tan A)/(1 – tan2A)']
             for i in range(len(cx)):
                  print(f'{i+1}.{cx[i]}')

             print()
             print()
             print('Triple Angle Formulas:')
             print('---------------------')
             print()
             cx=['sin 3A = 3 sinA – 4 sin3A','cos 3A = 4 cos3A – 3 cos A','tan 3A = [3 tan A – tan3A]/[1 − 3 tan2A]']
             for i in range(len(cx)):
                  print(f'{i+1}.{cx[i]}')


         elif j==10:
            print('Circles')
            print('-------')
            print()
            print('Circumference of a circle = 2 π r. Area of a circle = π r. Arc length of sector of circle with radius r and angle θ is ( θ/360) x 2 π r. The area of sector of a circle with radius 'r' and θ angle = ( θ/360) x π r.')
            print('Area of a Sector of a Circle : (θ/360°)×πr^2')
            
         elif j==11:
            print('Constructions')
            print('-------------')
            print()
            print('To construct the perpendicular bisector of a given line segment. 3 To construct and angle of 30°, 45°, 60°, 90°, 120° at the initial point of a given ray')

         elif j==12:
            print('Areas Related to Circles')
            print('------------------------')
            print()
            print('The distance around the circle or the length of a circle is called its circumference or perimeter , Circumference (perimeter) of a circle = πd or 2πr , where d is a diameter and r is a radius of the circle and π = 227 , Area of a circle = πr2 , Area of a semicircle = 12 πr2 Area of quadrant = 14 πr2')
            print()
            cd=['Area of a circle = πr2','Area of a semicircle = 12 πr2','Area of quadrant = 14 πr2','Perimeter of a semicircle = πr + 2r','Area of the ring or an annulus = π (R + r) (R – r)','Length of the arc AB = 2πrθ3600 = πrθ1800','Area of sector OACBO = πr2θ3600','Area of sector OACBO = 12 (r × l)','Perimeter of sector OACBO = Length of arc AB + 2r = πrθ1800 + 2r']
            for cv in range(len(cd)):
                print(f'{cv+1}.{cd[cv]}')
                print()
            print()

         elif j==13:
            print('Surface Areas And Volumes')
            print('-------------------------') 
            print()
            print('A cuboid is a region covered by its six rectangular faces. The surface area of a cuboid is equal to the sum of the areas of its six rectangular faces.')
            print()
            c=['Cube','Cuboid','Cone','Sphere','Hemisphere','Cylinder','Frustum of a cone']
            cg=[['Curved surface area (CSA) of cube = 4a²', 'Total surface area (TSA) of cube = 6a²','Volume = a³ ( Note that all the sides of a cube are equal)'],['CSA = 2h(l + b)','TSA = 2 (lb + bh + hl)','Volume= lbh ( l, b, and h stands for length, breadth and height respectively)'],['Volume = 1/3πr²h'],['TSA = 4πr²','Volume = 4/3πr³'],['CSA = 2πr²','TSA = 3πr²','Volume = 2/3πr³'],['CSA = 2πrh','TSA = 2πr(r+h)','Volume = 2πr²h'],[ 'CSA = πL(r+R)','TSA = πL(R+r) + π(R²+r²)' , 'Volume = 1/3πHr²+R²+rR','L² = H² + (R-r)²']]
            for k in range(len(c)):
                print(f'{k+1}.{c[k]}')
                print()
                print('    'f'{cg[k]}')
                print()
            print()

         elif j==14:
            print('Statistics')
            print('----------')
            print()
            print('Statistics is the study of collecting, classifying, arranging, and interpreting numerical data in a clear way. Statistics interprets the data and estimates possible results')

         elif j==15:
            print('Probability')
            print('----------')
            print()
            print('Probability of an Event = Number of Favorable Outcomes / Total Number of Possible Outcomes.')

    elif i2=='Social science'.lower():
         print('Streams of Social science')
         print('-------------------------')
         print()

         soc=['History - India and Contemporary World II','Geography - Contemporary India II','Political Science - Democratic Politics II','Economics - Understanding Economic Development']
         for k in range(len(soc)):
             print(f'{k+1}.{soc[k]}')
             print()
         print()        
         j=input("Type 'H' for History , Type 'G' for Geography , Type 'P' for Political Science , Type 'E' for Economics:")
         print()
         if j=='h'.lower():
             hist=['The Rise of Nationalism in Europe','Nationalism in India','The Making of a Global World','The Age of Industrialisation','Print Culture and the Modern World']
             print('History_info')
             print('------------')
             print()
             for l in range(len(hist)):
                 print(f'{l+1}.{hist[l]}')
                 print()
         elif j=='g'.lower():
             geo=[ 'Resources And Development','Forest And Wildlife Resources','Water Resources','Agriculture','Minerals And Energy','Manufacturing Industries','Lifelines Of National Economy']
             print('Geography_info')
             print('------------')
             print()
             for l in range(len(geo)):
                 print(f'{l+1}.{geo[l]}')
                 print()
         elif j=='p'.lower():
            pol=[ 'Power Sharing','Federalism','Democracy Diversity','Gender Religion Caste','Popular Struggles And Movements','Political Parties','Outcomes Of Democracy','Challenges To Democracy']
            print('Geography_info')
            print('------------')
            print()
            for l in range(len(pol)):
                print(f'{l+1}.{pol[l]}')
                print()
         elif j=='e'.lower():
            eco=['Development','Sectors Of Indian Economy','Money And Credit','Globalisation And Indian Economy','Consumer Rights']
            print('Economics_info')
            print('------------')
            print()
            for l in range(len(eco)):
                print(f'{l+1}.{eco[l]}')
                print()
