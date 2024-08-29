import tkinter as tk
import random 
import  pygame as pg



pg.mixer.init()




title_font = ("Arial", 50)
question_font = ("Arial", 30)
button_font = ("Arial", 20)
label_font = ("Arial", 18)

game_1_title = 'أسئلة دينية عامة'
game_2_title= 'لعبة من القائل في الآية'
game_3_title = 'لعبة من المقصود في الآية'


questions_dict = {
    "أقسام الماء": [
        "طهور، طاهر ونجس",  # Correct answer
        "طاهر، نقي و نجس",
        "طاهر و نجس",
        "طهور ونجس",
        "level 1",
        "طهور، طاهر ونجس"  # Correct answer at the end
    ],
    "معنى التيامن": [
        "التيمم",
        "البدأ اليمين في الأعمال الشريفة",  # Correct answer
        "الأكل باليمين",
        "جميع الإجابات صحيحة",
        "level 1",        
        "البدأ اليمين في الأعمال الشريفة"  # Correct answer at the end
    ],
    "متى يشرع سجود السهو؟": [
        "عند الشك فقط",
        "عند الزيادة والنقص والشك عمدا",
        "عند الزيادة و النقص والشك سهوا",  # Correct answer
        "عند الزيادة والنقص سهوا فقط",
        "level 1",
        "عند الزيادة و النقص والشك سهوا"  # Correct answer at the end
    ],
    "هل يجوز قتل نفس مسلمة مقابل الحفاظ على نفسك؟": [
        "حرام ولا يجوز",  # Correct answer
        "جائز",
        "مكروه",
        "مستحب",
        "level 1",
        "حرام ولا يجوز"  # Correct answer at the end
    ],
    "أقسام النجاسات": [
        "نجاسة عينية ظاهرة وحكمية باطنة",
        "كل الإجابات خاطئة",
        "نجاسة ظاهرة وباطنة",
        "نجاسة عينية وحكمية",  # Correct answer
        "level 1",
        "نجاسة عينية وحكمية"  # Correct answer at the end
    ],
    "من هم الأعراب؟": [
        "أهل البوادي من العجم",
        "أهل الحواضر من العرب",
        "أهل البوادي من العرب",  # Correct answer
        "أهل الحواضر من العجم",
        "level 1",
        "أهل البوادي من العرب"  # Correct answer at the end
    ]


}


game_2_dict = {
    "من القائل: يَا بَنِيَّ إِنَّ اللَّهَ اصْطَفَىٰ لَكُمُ الدِّينَ فَلَا تَمُوتُنَّ إِلَّا وَأَنتُم مُّسْلِمُونَ": [
        "إبراهيم عليه السلام", 
        "إسماعيل عليه السلام", 
        "موسى عليه السلام", 
        "يعقوب عليه السلام", # Correct answer
        "level 2",
        "يعقوب عليه السلام" # Correct answer at the end
    ],
    "من القائل: قَالَ يَٰقَوۡمِ ٱتَّبِعُواْ ٱلۡمُرۡسَلِينَ ۝ ٱتَّبِعُواْ مَن لَّا يَسۡـَٔلُكُمۡ أَجۡرٗا وَهُم مُّهۡتَدُونَ": [
        "الرسل الثلاثة",    
        "رجل يسعى", # Correct answer
        "بنيامين", 
        "الحواريون", 
        "رجل يسعى" # Correct answer at the end
    ],
    "من القائل: فَاغْفِرْ لِلَّذِينَ تَابُوا وَاتَّبَعُوا سَبِيلَكَ": [
        "حملة عرش الرحمن", # Correct answer
        "الرسل", 
        "الملائكة", 
        "لا توجد إجابة", 
        "level 2",
        "حملة عرش الرحمن"# Correct answer at the end
    ],
    "من القائل: لَأَحْتَنِكَنَّ ذُرِّيَّتَهُ إِلا قليلًا ": [
        "النمرود", 
        "فرعون", 
        "إبليس", # Correct answer
        "أبو لهب", 
        "level 2",
        "إبليس"# Correct answer at the end
    ],



    "من القائل: قَدْ جِئْتُكُم بِبَيِّنَةٍ مِّن رَّبِّكُمْ فَأَرْسِلْ مَعِيَ بَنِي إِسْرَائِيلَ ":[
        "هارون عليه السلام", 
        "يحيى عليه السلام", 
        "عيسى عليه السلام", 
        "موسى عليه السلام", 
        "level 2",
        "موسى عليه السلام" # Correct answer at the end
    ],


    
    "من القائل: قَالَ قَدْ وَقَعَ عَلَيْكُم مِّن رَّبِّكُمْ رِجْسٌ وَغَضَبٌ ۖ": [
        "صالح عليه السلام", 
        "هود عليه السلام", # Correct answer
        "شعيب عليه السلام", 
        "لوط عليه السلام", 
        "level 2",
        "هود عليه السلام" # Correct answer at the end
    ]
}


game_3_dict = {
    " الَّذِينَ كَذَّبُوا شُعَيْبًا كَانُوا هُمُ الْخَاسِرِينَ ": [
        "قوم عاد",
        "قوم ثمود",
        "لا توجد إجابة",
        "أهل مدين",  # Correct answer
        "level 3",
        "أهل مدين"  # Correct answer at the end
    ],
    " تِلْكَ الْقُرَىٰ نَقُصُّ عَلَيْكَ مِنْ أَنبَائِهَا  ": [
        "إبراهيم عليه السلام",
        "محمد عليه الصلاة والسلام",  # Correct answer
        "موسى عليه السلام",
        "عيسى عليه السلام",
        "level 3",
        "محمد عليه الصلاة والسلام"  # Correct answer at the end
    ],
    " وَيَسْأَلُونَكَ عَنِ الرُّوحِ قُلِ الرُّوحُ مِنْ أَمْرِ رَبِّي وَمَا أُوتِيتُم مِّنَ الْعِلْمِ إِلَّا قَلِيلًا ": [
        "اليهود",  # Correct answer
        "قريش",
        "الصحابة رضوان الله عليهم",
        "النصارى",
        "level 3",
        "اليهود"  # Correct answer at the end
    ],
    " يَمْشُونَ مُطْمَئِنِّينَ لَنَزَّلْنَا عَلَيْهِم مِّنَ السَّمَاءِ مَلَكًا رَّسُولًا ": [
        "الملائكة",  # Correct answer
        "بني إسرائيل",
        "قوم عاد",
        "قوم ثمود",
        "level 3",
        "الملائكة"  # Correct answer at the end
    ],
    " قُلْ لا تُسْأَلُونَ عَمَّا أَجْرَمْنَا وَلا نُسْأَلُ عَمَّا تَعْمَلُونَ": [
        "الكفار",
        "اليهود",
        "أمة محمد صل الله عليه وسلم",  # Correct answer
        "النصارى",
        "level 3",
        "أمة محمد صل الله عليه وسلم"  # Correct answer at the end
    ],
    " لَوْلَا أَنتُمْ لَكُنَّا مُؤْمِنِينَ ": [
        "المستضعفين",
        "المستكبرين",  # Correct answer
        "اليهود",
        "المنافقين",
        "level 3",
        "المستكبرين"  # Correct answer at the end
    ]
}

dev_info = 'rayanereda90@gmail.com'


menu_title = "اختبر معلوماتك الآن"

mode_title = "حدد نوع اللعبة"





Questions = list(questions_dict.keys())

game_2_questions = list(game_2_dict.keys())

game_3_questions = list(game_3_dict.keys())


class Gui:
    def __init__(self):
        self.root = tk.Tk()
        
        self.new_best_score_1 = self.load_best_score('best_score_1.txt')
        self.new_best_score_2 = self.load_best_score('best_score_2.txt')
        self.new_best_score_3 = self.load_best_score('best_score_3.txt')


        self.Q_random = random.choice(Questions)

        self.root.title("اختبارات دينية")
        self.root.state('zoomed')
        
        self.Title = tk.Label(self.root, text = menu_title, font = title_font)
        self.Title.pack()

        self.frame_menu = tk.Frame(self.root)

        self.start_games = tk.Button(self.frame_menu, text = 'بدأ اللعب', font = ("Hacen Beirut light", 20), command= self.start_game_cmd)
        self.start_games.pack(pady=20)
        
        self.score_best = tk.Button(self.frame_menu, text = 'أعلى نقاط', font = ("Hacen Beirut light", 20), command = self.best_score)
        self.score_best.pack(pady=20)


        self.settings = tk.Button(self.frame_menu, text = 'ضبط الإعدادات', font = ("Hacen Beirut light", 20), command= self.settings_widget)
        self.settings.pack(pady=20)

        self.dev_info = tk.Button(self.frame_menu, text = 'معلومات عن المطور', font = ("Hacen Beirut light", 20) , command = self.info_dev)
        self.dev_info.pack(pady=20)

        self.frame_mode = tk.Frame(self.root)

        self.game_1 = tk.Button(self.frame_mode, text = 'أسئلة دينية عامة', font = ("Hacen Beirut light", 20), command= lambda: self.game_level(Questions, questions_dict, game_1_title, self.new_best_score_1))

        self.game_2 = tk.Button(self.frame_mode, text = 'لعبة من القائل في الآية', font = ("Hacen Beirut light", 20), command = lambda: self.game_level(game_2_questions, game_2_dict, game_2_title, self.new_best_score_2))

        self.game_3 = tk.Button(self.frame_mode, text= "لعبة من المقصود في الآية", font = ("Hacen Beirut light", 20), command= lambda: self.game_level(game_3_questions, game_3_dict, game_3_title, self.new_best_score_3))

        self.back = tk.Button(self.root, text = "الرجوع للقائمة", command= lambda:self.back_button( self.frame_mode, menu_title), font = ("Hacen Beirut light", 15))

        self.frame_best_score = tk.Frame(self.root)

        self.best_score_1 = tk.Label(self.frame_best_score, text=f'اللعبة الأولى: {self.new_best_score_1}', font= ("Hacen Beirut light", 25, "bold") )
        self.best_score_2 = tk.Label(self.frame_best_score, text=f'اللعبة الثانية: {self.new_best_score_2}', font= ("Hacen Beirut light", 25, "bold") )
        self.best_score_3 = tk.Label(self.frame_best_score, text=f'اللعبة الثالثة: {self.new_best_score_3}', font= ("Hacen Beirut light", 25, "bold") )
        self.reset_best_score_btn = tk.Button(self.frame_best_score, text="تصفير النقاط",font= ("Hacen Beirut light", 15), command= self.reset_best_score)

        self.frame_settings = tk.Frame(self.root)
        
        self.sound_state= tk.IntVar()
        self.check_sound = tk.Checkbutton(self.frame_settings, text='أوقف صوت اللعبة', variable=self.sound_state)

        
        
        self.frame_info = tk.Frame(self.root)

        self.info_label = tk.Label(self.frame_info, text = dev_info, font= ('Yekan', 40))




        self.frame_parent = tk.Frame(self.root)

        self.frame_timeup = tk.Frame(self.root)

        self.random_question = tk.Label(self.frame_parent, text = self.Q_random, font =question_font )
        
        self.correct_label = tk.Label(self.root, text = 'إجابة صحيحة', font=   ("Hacen Liner Print-out", 15) )
        self.incorrect_label = tk.Label(self.root, text = 'إجابة خاطئة', font=   ("Hacen Liner Print-out", 15) )

        self.frame = tk.Frame(self.frame_parent)
        self.frame.columnconfigure(0, weight= 1)
        self.frame.columnconfigure(1, weight= 1)
        
        self.button1 = tk.Button(self.frame, text = None, font = button_font, command=  None) 
        self.button1.grid(row = 0, column= 0, sticky= tk.E+tk.W, padx= 20, pady=20)
        
        self.button2 = tk.Button(self.frame, text = None, font = button_font,  command= None) 
        self.button2.grid(row = 0, column= 1, sticky= tk.E+tk.W, padx= 20, pady=20)
        
        self.button3 = tk.Button(self.frame, text = None, font = button_font,  command= None)
        self.button3.grid(row = 1, column= 0, sticky= tk.E+tk.W, padx= 20, pady=20)
        
        self.button4 = tk.Button(self.frame, text = None, font = button_font,  command= None)
        self.button4.grid(row = 1, column= 1, sticky= tk.E+tk.W, padx= 20, pady=20)

        self.frame.pack(fill= 'x')
        self.I_answer_num = 0

        self.is_running = False
        self.timer_id = None


        self.score_var = 0
        self.score_pack = tk.Label(self.frame_parent, text = f"النقاط: {self.score_var}", font = ("Arial", 20))
        
        
        self.current_time = 20
        self.timer_pack = tk.Label(self.frame_parent, text = f"العداد التنازلي: {self.current_time}", font = ("Arial", 20))


        self.score_total = tk.Label(self.frame_timeup, text= f"النقاط: {self.score_var}", font= ("Arial", 40))
        self.time_up = tk.Label(self.frame_timeup, text= "ركز أكثر", font = ("Arial", 30))
        self.retry = tk.Button(self.frame_timeup, text= "حاول مجددا", command= lambda: self.retry_game(game=Questions, game_dict= questions_dict, game_level_title=None), font = ("Arial", 20))

        self.frame_menu.pack(fill="both")

        self.game_clicked = False


        self.correct_sound = pg.mixer.Sound(r"C:\Users\MSI\Downloads\correct_sound_effect_1.mp3")
        self.button_click = pg.mixer.Sound(r"C:\Users\MSI\Downloads\button_click.mp3")
        
        self.root.mainloop()

    def text_based_on_score(self):
        if self.score_var <= 0:
            text = "ركز أكثر"
        else:
            text = self.Great_bad_score()
        self.time_up.config(text = text)

    def Great_bad_score(self):
        if 0<self.score_var <50 :
            return '!لا بأس'
        elif self.score_var >= 50:
            return "!عمل ممتاز" 
    

    def score_C_answer(self, game, game_dict):
        
        self.score_var += 2
        
        self.score_pack.config(text=f"النقاط: {self.score_var}")

        self.root.after(50, lambda:self.update(game, game_dict))

        self.score_total.config(text= f"النقاط: {self.score_var}")
        if self.sound_state.get() == 0:
            self.correct_sound.play()
 
    

    def score_I_answer(self):
        self.score_var -= 1
        self.I_answer_num += 1
        self.score_pack.config(text=f"النقاط: {self.score_var}")
        if self.sound_state.get() == 0:
            self.button_click.play()


    
    def back_button(self, next_frame, Title):
        self.back.pack_forget()
        for widgets in self.frame_menu.winfo_children():
            widgets.pack(pady=20)


        for i in next_frame.winfo_children():
            i.pack_forget() 

        if self.sound_state.get() == 0:
            self.button_click.play()
        
        self.frame_menu.pack(before = next_frame, fill= "both")
        self.Title.config(text = Title)
            
        try:   
            if self.game_clicked == True:
                self.root.after_cancel(self.timer_id)
        except ValueError:
            print("value error")
        self.score_var = 0
        self.I_answer_num = 0
        self.score_pack.config(text = f"النقاط: {self.score_var}")
        self.game_clicked = False
    
    
    def start_game_cmd(self):
        for widgets in self.frame_menu.winfo_children():
            widgets.pack_forget()
        
        for i in self.frame_mode.winfo_children():
            i.pack(pady=20, side = "top") 
        
        self.frame_mode.pack(fill="both", expand= True, before = self.frame_menu)
        self.Title.config(text = mode_title)

        if self.sound_state.get() == 0:
            self.button_click.play()

        self.back.pack(pady = 20, before= self.frame_menu)
        self.back.config(command=lambda : self.back_button(self.frame_mode, menu_title))
       
    
    def game_level(self, game_questions_list, game_questions_dict, game_title, best_score):
        self.Q_random = random.choice(game_questions_list)

        self.frame.pack(fill='x')
        for widgets in self.frame_parent.winfo_children():
            if widgets == self.score_pack:
                widgets.pack(side='right', pady = 10, padx=20)
            elif widgets == self.timer_pack:
                widgets.pack(side = 'left', pady = 10, padx = 20)
            elif widgets == self.random_question:
                widgets.pack(before = self.frame, pady=20)
            else:
                widgets.pack()
        
        self.Title.config(text = game_title)

        if self.sound_state.get() == 0:
            self.button_click.play()
        
        for i in self.frame_mode.winfo_children():
            i.pack_forget()

        self.frame_parent.pack(before= self.frame_mode, fill='both', expand= True)
        self.timer(20)
        self.back.pack(after = self.frame_parent)
        self.back.config(command= lambda : self.back_button(self.frame_parent, menu_title))
        self.random_question.config(text = self.Q_random)

        self.button1.config(text = game_questions_dict[self.Q_random][0], command= lambda: self.game_button(self.button1.cget("text"), game_questions_dict, game_questions_list, best_score))
        self.button2.config(text = game_questions_dict[self.Q_random][1], command= lambda: self.game_button(self.button2.cget("text"), game_questions_dict, game_questions_list, best_score))
        self.button3.config(text = game_questions_dict[self.Q_random][2], command= lambda: self.game_button(self.button3.cget("text"),  game_questions_dict, game_questions_list, best_score))
        self.button4.config(text = game_questions_dict[self.Q_random][3], command= lambda: self.game_button(self.button4.cget("text"),  game_questions_dict, game_questions_list, best_score))
        
        self.retry.config(command = lambda: self.retry_game(game_questions_list, game_questions_dict, game_title))
        self.game_clicked = True
    
    
    
    def settings_widget (self):
        for widgets in self.frame_menu.winfo_children():
            widgets.pack_forget()
        
        for i in self.frame_settings.winfo_children():
            i.pack(anchor='center', pady=20)
        self.frame_settings.pack(before = self.frame_menu)
        self.back.pack(before = self.frame_menu)
        self.back.config(command = lambda: self.back_button(self.frame_settings, menu_title))

        if self.sound_state.get() == 0:
            self.button_click.play()

    def info_dev(self):
        for widgets in self.frame_menu.winfo_children():
            widgets.pack_forget()
        
        for i in self.frame_info.winfo_children():
            i.pack(pady = 20)
        self.frame_info.pack(before=self.frame_menu)
        self.back.pack(before= self.frame_menu)
        self.back.config(command = lambda: self.back_button(self.frame_info, menu_title))
        self.Title.config(text = ":من طرف")
        
        if self.sound_state.get() == 0:
            self.button_click.play()
        
        
    
    def best_score(self):
        
        
        for widgets in self.frame_best_score.winfo_children():
            widgets.pack(pady=20)
        self.frame_best_score.pack(before = self.frame_menu)
        self.back.pack(before=self.frame_menu)
        self.back.config(command = lambda : self.back_button(self.frame_best_score, menu_title))

        self.Title.config(text="أعلى معدل")
        self.best_score_1.config(text= f"اللعبة الأولى: {self.new_best_score_1}")
        self.best_score_2.config(text= f"اللعبة الثانية: {self.new_best_score_2}")
        self.best_score_3.config(text= f"اللعبة الثالثة: {self.new_best_score_3}")
        
        for widgets in self.frame_menu.winfo_children():
            widgets.pack_forget()

        if self.sound_state.get() == 0:
            self.button_click.play()

    def reset_best_score(self):
        try:
            for i in ['best_score_1.txt', 'best_score_2.txt', 'best_score_3.txt']:
                with open(i, 'w') as file:
                    file.write('0')
            self.new_best_score_1 = self.load_best_score('best_score_1.txt')
            self.new_best_score_2 = self.load_best_score('best_score_2.txt')
            self.new_best_score_3 = self.load_best_score('best_score_3.txt')
            self.best_score_1.config(text= f'اللعبة الأولى: {self.new_best_score_1}')
            self.best_score_2.config(text=f'اللعبة الثانية: {self.new_best_score_2}')
            self.best_score_3.config(text=f'اللعبة الثالثة: {self.new_best_score_3}')
        except FileNotFoundError:
            return "Error"

    def timer(self, current_time):
        if self.is_running:
            self.root.after_cancel(self.timer_id)  

        self.timer_pack.config(text=f"العداد التنازلي: {current_time}")

        if current_time > 0:    
            self.timer_id = self.root.after(1000, self.timer, current_time - 1)
            self.is_running = True
        elif current_time <= 0:
            self.score_total.config(text= f"النقاط: {self.score_var}")
            self.is_running = False
            self.game_over()
            self.window_clear()
            
            self.game_check(self.Title.cget("text"))
            
            if self.I_answer_num == 2:
                self.Title.config(text="أخطأت مرتين")
            else:
                self.Title.config(text = "انتهى الوقت")
            
        

            
    def game_over(self):
        for widgets in self.frame_timeup.winfo_children():
            widgets.pack()
        
        self.frame_timeup.pack(fill= "both", before= self.frame_parent)
        self.back.pack(before=self.frame_parent )
        self.back.config(command=lambda:self.back_button(self.frame_timeup, menu_title))
            
        
            
            
    def window_clear(self):
        for widgets in self.frame_parent.winfo_children():
            widgets.pack_forget()

    
    
    def retry_game(self, game, game_dict, game_level_title):
        self.is_running = False
        self.I_answer_num = 0
        for widgets in self.frame_parent.winfo_children():
            
            if widgets == self.score_pack :
                widgets.pack(side='right', pady= 10, padx=20)
            elif widgets == self.timer_pack:
                widgets.pack(side= 'left', pady= 10, padx=20)
            elif widgets == self.random_question:
                widgets.pack(pady= 20)
            else:
                widgets.pack(fill="both")

        for i in self.frame_timeup.winfo_children():
            i.pack_forget()

        self.frame_parent.pack(before = self.frame_timeup)
        self.back.pack(before= self.frame_timeup)
        self.back.config(command = lambda: self.back_button(self.frame_parent, menu_title))
        self.score_var = 0
        self.score_pack.config(text=f"النقاط: {self.score_var}")
        self.score_total.config(text=f"النقاط: {self.score_var}")
        self.timer(self.current_time)
        #Problem here!
        
        
        self.Title.config(text = game_level_title)
        
        
        self.update(game=game, game_dict=game_dict)



        if self.sound_state.get() == 0:
            self.button_click.play()

        
    def update(self, game, game_dict):
        if hasattr(self, 'timer_id'):
            self.root.after_cancel(self.timer_id)
        
        self.I_answer_num = 0
        self.is_running = False
        self.Q_random = random.choice(game)
        self.random_question.config(text = self.Q_random)
        self.button1.config(text=game_dict[self.Q_random][0])
        self.button2.config(text = game_dict[self.Q_random][1])
        self.button3.config(text = game_dict[self.Q_random][2])
        self.button4.config(text = game_dict[self.Q_random][3])
    #   self.next_button.config(state= "disabled")
        if not self.is_running :
            self.timer(self.current_time)

    def load_best_score(self, file_type):
        try:
            with open(file_type, 'r') as file:
                return  int(file.read().strip())
        except FileNotFoundError:
            return 0

    def update_best_score(self, file, score):
        if score< self.score_var:
            score = self.score_var
            with open(file, 'w') as file:
                file.write(str(score))
            return self.score_var
        return score
        
    

    def game_check(self, game_type):
        if game_type == "أسئلة دينية عامة":
            self.new_best_score_1 = self.update_best_score('best_score_1.txt', self.new_best_score_1)
            self.best_score_1.config(text=f'اللعبة الأولى: {self.new_best_score_1}')
        elif game_type == "لعبة من القائل في الآية":
            self.new_best_score_2 = self.update_best_score('best_score_2.txt', self.new_best_score_2)
            self.best_score_2.config(text=f'اللعبة الثانية: {self.new_best_score_2}')
        elif game_type == "لعبة من المقصود في الآية":
            self.new_best_score_3 = self.update_best_score('best_score_3.txt', self.new_best_score_3)
            self.best_score_3.config(text=f'اللعبة الأولى: {self.new_best_score_3}')



    def game_check_answer(self, selected_button, game_dict, game_list, best_score):
        correct_answer = game_dict[self.Q_random][-1]
        if correct_answer == selected_button:
            self.is_correct = True
            self.score_C_answer(game = game_list, game_dict = game_dict)
        
        else:
            self.is_correct = False
            self.score_I_answer()
            if self.I_answer_num == 2:
                if best_score < self.score_var:
                    self.game_check(self.Title.cget("text"))
                self.timer(0)

        self.score_total.config(text= f"النقاط: {self.score_var}")
        self.text_based_on_score()

    
        
    def game_button(self, btn_index, game_dict, game_list, best_score):
        self.game_check_answer(btn_index, game_dict, game_list, best_score)
        if btn_index == game_dict[self.Q_random][-1]:
            self.correct_label.place(relx=0.5, rely=0.5, anchor="center")
            self.root.after(1500, self.correct_label.place_forget)
        else:
            self.incorrect_label.place(relx=0.5, rely=0.5, anchor="center")
            self.incorrect_label.after(1500, self.incorrect_label.place_forget)


    
Gui()
