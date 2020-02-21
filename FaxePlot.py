import pandas as pd

class readfile():
    def __init__(self,navn):
        self.navn=navn
        self.makefile()
        
    def makefile(self):
        db_ind=[]
        with open(self.navn) as f:
            for line in f: 
                line=line.strip('\t\n')
                line=line.split('\t')
                db_ind.append(line)

        col_names=["nature", "dist", "country", "customer", "shipto", "material", "process", "mduse", "year", "month", "actual", "budget"] 
        self.db=pd.DataFrame(db_ind,columns=col_names)
        self.db[["customer","shipto","material","year","month","actual","budget"]] = self.db[["customer","shipto","material","year","month","actual","budget"]].apply(pd.to_numeric, errors='coerce')
        self.db=self.db.fillna(0)
    
    def getfile(self):
        return self.db

class makeplots():
    def __init__(self,db):
        self.db=db
        self.myplot()    
        
    def myplot(self):
        #Sætte index til måned
        db=self.db.set_index(["month"])
        #Vælge år
        db=db.loc[(db["year"]==2018),:]
        
        #Trække serier ud med hydratprodukter
        hyk_db=db.loc[(db["material"]==92),:]
        bag_db=db.loc[(db["material"]==87),:]
        bb_db=db.loc[(db["material"]==2160),:]
        
        #Summere per måned - måned er index
        plot1=hyk_db["actual"].sum(level="month")
        plot2=bag_db["actual"].sum(level="month")
        plot3=bb_db["actual"].sum(level="month")
        
        #merge kolonner
        hyk_total=pd.concat([plot1,plot2,plot3],axis=1)
        
        hyk_total.columns=["bulk","bag","bigbag"]
        
        hyk_total["total"]=hyk_total["bulk"]+hyk_total["bag"]+hyk_total["bigbag"]
        
        print(hyk_total)
        
        hyk_total.plot()


class materialeplots():
    def __init__(self,db,year,mat_list,col_names,totals):
        self.db=db
        self.year=year
        self.mat_list=mat_list
        self.col_names=col_names
        self.totals=totals
        self.makeplot()    
        
    def makeplot(self):
        #Sætte index til måned
        db=self.db.set_index(["month"])
        
        #Vælge år
        db=db.loc[(db["year"]==self.year),:]

        #liste per materiale [[mat 0 pandas liste][mat 1 liste] [mat2 liste]...]
        db_mat=[]
        for i in range(len(self.mat_list)):
            db_mat.append(db.loc[(db["material"]==self.mat_list[i]),:])
            
        print(db_mat[0].head())
        
        
        #sum per måned for første materiale [0]    
        #print(db_mat[0]["actual"].sum(level="month"))
        
        #Summere per måned - måned er index
        plot_line=[]
        for i in range(len(self.mat_list)):
            plot_line.append(db_mat[i]["actual"].sum(level="month"))
         
        #print(plot_line)
        
        #merge kolonner
        hyk_total=plot_line[0]
        for i in range(1,len(plot_line)):
            hyk_total=pd.concat([hyk_total,plot_line[i]],axis=1)        
     
        hyk_total.columns=self.col_names
        
        #Hvis ønsket så kolonne med totaler
        if self.totals:
            hyk_total["total"]=hyk_total[self.col_names[0]]
        
            for i in range(1,len(plot_line)):
                hyk_total["total"]+=hyk_total[self.col_names[i]]          
       
        print(hyk_total)
        
        hyk_total.plot()


db=readfile("FaxePandas.txt").getfile()

mat_list=[92,87,2160]
col_names=["bulk","bag","bigbag"]
#mat_list=[3207,3535]
#col_names=["10mm","6mm"]
year=2018
totals=True

#makeplots(db)
materialeplots(db,year,mat_list,col_names,totals)

