#Adam and Eve
#generating family tree
#Person_class
 
import random
femalegothnames =' adosinda amalafrida amalasontha amalasuintha amalaswinth amalaswintha amalina amalwara amelina avagisa avina brenhilda brunichild brunihild chlodoswintha fredegonda gailavira gailesvintha garsendis geleswintha gelvira goisvintha gosvintha hermangild hermesind heva hilduara liuva matasvintha radegond radegonda riciberga '
malegothnames=  ' adalfuns adalrik alaric alarica alhreiks alhvaharyis amalareiks andagis ansila arareiks athalagild athalareiks athalaric athanagild athanareiks athanaric atta audo audoacer audvakr austraguta ausvinthus avagis badwila beremud botheric childefonsus chindasvinth chindaswintha dag eboric ebrimuth ediulf egica eiriks ermanaric ermenigeld ermingild erminigeld euric eutharic evermud evoric ferhonanths frideger frithigern fritigern geberic gisalrico giselric haduswinth hairuwulf hathus hermanaric hermanrich hermangild hermengild hermenigildo hildefons hildefuns hunuil ildefons ildefónso kindaswinth kunimund leovigild leovigildo liuva odoacer odovacar recimir richila ricimar roderic suintila svinthila tautila theoderic theodoric theudefred theudis thiudareiks thorismund thurismod thurismund tius totila ulphilas unwen veremundo vermundo vulfila wallia '
femalewelshnames= ' aderyn aeron aerona aeronwen aeronwy afanen afon alis alison anarawd angharad angharat angharawd anwen anwyn aranrhod arianrhod bethan betrys blodeuedd blodeuwedd blodeuyn blodwedd blodwen braith brangwen brangwy branwen branwenn brava briallen brin bron brongwyn bronwen bronwyn bryn brynn brynne cadi caron carys catrin ceinwen ceri ceridwen cerridwyn cerys crearwy creiddylad creirwy crystin danbrann delwyn delyth deryn dilwen dilys dôn dwyn dwynwen dwynwyn dylis efa eigr eigyr eilian eiluned eilwen eira eirian eirlys eirwen elain elen eleri eluned emlyn enfys enid enit esyllt eurwen ffion ffraid gaenor generys gladys glaudusa glaw glenda glenice glenys glynis goleuddydd guendolen gwawr gwen gwenda gwendolen gwendoline gwendolyn gweneth gwenevak gwenfrewi gwenhwyvach gwengwyvar gwenith gwenllian gwenhwyvar gwenn gwenneth gwenyth gwladus gwyn gwynedd gwyneira gwyneth gwynn habren haf hafren hefina heledd heulog heulwen hyledd lin linn lleulu llewella llinos lowri luned lyn lynn lynne mair mairwen mallt mared marged mari megan meinir meinwen mererid modron morgan morgana morwen morwenna myf myfanwy nerys nest nesta nia nimue olwen olwin olwyn owena paderau reannon rhamantus rhian rhiannon rhianon rhianu rhianwen rhonwen rhosyn riannon seren siân siana siani siôned siwan talaith tarren tegwen tegwen terrwyn tiwlip ysbail '
malewelshnames=' aeron afon aled alun anarawd andras aneirin aneurin arawn arthfael arvel arwel awstin bedwyr bel beli berwyn braith bran brenin brenin brin broderick brychan bryn brynmor brynn cadell cadeyrn cadfael cadfan cadoc cadomedd cadwalader cadwallader cadwgawn caerwyn cai caradawc caradawg caradoc caradog carwyn catmail cattegirn cefin celyddon celyn ceri cledwyn culhwch cynddelw cynwrig cystenian dafydd dai deiniol delwyn derog dewi dewydd dillon dilwyn drystan the dyfed dyl dylan eilian einion elian elidyr elis elisud elyan emlyn emrys emyr enfys ercwlff eugein euguein eurig ewein floyd folant gareth garreth garth geraint gerallt gethen gethin glaw glyn glyndwr glynn gofannon gorlassar goronwy govannon griffin grigor gripiud grippiud gronw gruffin gruffud gruffudd gruffydd grwn guorthigern guorthigirn guto gwalchgwyn gwalchmai gwalchmei gwalltafwyn gwallter gwil gwilim gwillym gwilym gwledig gwrgenau gwri gwrtheyrn gwyn gwynedd gwynfor gwynn gwythyr hadyn halwn halwyn harri haul heddwyn hefeydd hefin heilyn helyan henbeddestyr henwas heulog henwyneb hopcyn huarwar huarwor huw hywel iago ianto iau idris idwal iefan iestyn ieuan ifan ifor ilar illtud illtyd ioan iolo iolyn iorwerth islwyn ithel iwan kai lleu llew short welsh llewellyn llewelyn lloyd llyr llywellyn llywelyn logres loyd mabon macsen madoc madog maldwyn march maredudd mawrth maxen meical meirion mercher meredydd merfyn merrion meuric meurig mihangel moesen morgan mostyn myrddin neifion neirin nudd nye ofydd oswallt ouen owain owein owen owin owyn paderau padrig parry pedr penllyn pryce pryderi pwyll renfrew rheinallt rhisiart rhobert rhodri rhydderch rhys rys robyn rolant sadwrn sawyl scilti seissylt selyf siarl sieffre siencyn sion sior siors siorus siorys steffan taffy talfryn taliesin teirtu tomos trahaearn trefor tudur tudyr twedwr twm uchdryd urbgen urien uwain vaughan vaughn wmffre wmfre wyn wynfor wynn wynne yale ysbaddaden '
 
class MarkovGenerator:
    def __init__(self,dicti=' as long as the iterator returns the same thing a list would during iteration '):
        derivationslist=[(dicti[i:i+2],dicti[i+2]) for i in range(len(dicti)-2)]
        self.lexicon={}
        #couldn't find a nice lambda fuction derivation
        for i in derivationslist:
            digram,prod=i
            if digram not in self.lexicon:
                self.lexicon[digram]=[]
            self.lexicon[digram].append(prod)  
    def Spew_word(self):
        #and there is a lambda
        filfun=lambda x: x[0]==' '
        initials=[i for i in filter(filfun,[j for j in self.lexicon])]
        starting=random.choice(initials)
        production=starting
        #cannot find nice, smart derivations, go the stupid way
        while starting[1]!=' ':
            newsymbol=random.choice(self.lexicon[starting])
            production+=newsymbol
            starting=starting[1]+newsymbol
        return production.strip().title()
 
class Person:
    def __init__(self,gen_name="Random",gen_sex="male",gen_sexual_orientation="hetero",gen_body=50,gen_mind=50,gen_spirit=50,gen_age=0):
        #we start with a very simple model here
        self.name=gen_name
        self.sex=gen_sex
        self.sexual_orientation=gen_sexual_orientation
        self.body=gen_body
        self.mind=gen_mind
        self.spirit=gen_spirit
        self.age=gen_age
        self.alive=True
        if gen_sex=="male":
            self.low_reproduction_limit=13
            self.high_reproduction_limit=90
        else:
            self.low_reproduction_limit=15
            self.high_reproduction_limit=50
    def age_a_year(self):
        self.age+=1
    def kill(self):
        self.alive=False
    def debug(self):
        print (self.name, " is a ",self.sex," ", self.sexual_orientation ," person")
        print ("Body:",self.body)
        print ("Mind:",self.mind)
        print ("Spirit:",self.spirit)
        print ("Age:", self.age)
 
#male and female created them
 
name_male=MarkovGenerator(malegothnames)
name_female=MarkovGenerator(femalegothnames)
adam=Person(name_male.Spew_word(),gen_age=33)
eve=Person(name_female.Spew_word(),gen_sex="female", gen_age=21)
adam.debug()
eve.debug()
