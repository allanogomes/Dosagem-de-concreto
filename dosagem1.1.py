# Allan de Oliveira Gomes - RA 2236362
# Maria Eduarda Simeão Wollmann - RA 1777637

import math
tipo = 0
while tipo != 3:
    print('Aplicativo de Dosagens de Concreto')
    tipo =int(input('Escolha o tipo de Dosagem: IPT [1] ABCP [2] sair [3]'))
    if tipo == 1:
        print('Tipo IPT: ')
        
        fc1 = float(input('Insira o fc1: '))
        fc2 = float(input('Insira o fc2: '))
        fc3 = float(input('Insira o fc3: '))
        ac1 = float(input('Insira o a/c1: '))
        ac2 = float(input('Insira o a/c2: '))
        ac3 = float(input('Insira o a/c3: '))
        m1 = float(input('Insira o m 1: '))
        m2 = float(input('Insira o m 2: '))
        m3 = float(input('Insira o m 3: '))
        me1 = float(input('Insira a ME 1 do cimento: '))
        me2 = float(input('Insira a ME 2 do cimento: '))
        me3 = float(input('Insira a ME 3 do cimento: '))
        argamassa = float(input('Insira o teor de argamassa: '))
    # mUnitariaBrita = float(input('Insira a massa unitária da brita'))
       # mEspecificaBrita = float(input('Insira a massa específica da brita'))
       # mUnitariaAreia = float(input('Insira a massa unitária da areia'))
       # mEspecificaAreia = float(input('Insira a massa específica da areia'))
       #  mEspecificaCimento = float(input('Insira a massa específica do cimento'))
        desvio = float(input('Insira o desvio padrão: '))
        fck1 = float(input('Insira o fck: '))
        print('------'*15)
        
        cimento1 = me1/(1.0+m1+ac1)
        cimento2 = me2/(1.0+m2+ac2)
        cimento3 = me3/(1.0+m3+ac3)
        
        b1 = math.log(fc1,10)*(2.0*ac1-ac2-ac3) + math.log(fc2,10)*(2.0*ac2-ac1-ac3) + math.log(fc3,10)*(2.0*ac3-ac1-ac2)
      #  print('b1 = ',b1)
        b2 = (2.0*(ac1**2.0 + ac2**2.0 + ac3**2.0)) - (2.0*(ac1*ac2+ac1*ac3+ac2*ac3))
      #  print('b2 = ',b2)
        b = (b1/b2)
        k2 = 10.0**(-b)
        print('b = ',b)
        print('K2 = ',k2)
        
        c = (1.0/3.0)*(math.log(fc1,10)+math.log(fc2,10)+math.log(fc3,10)-(b*(ac1+ac2+ac3)))
        k1 = 10.0**c
        print('c = ',c)
        print('K1 = ',k1)
        
        fcd1 = fck1 + 1.65*desvio
        print('Fcd = ',fcd1)
        
        acfinal = (-1.0/b)*math.log(k1/fcd1,10)
        print('a/c = ',acfinal)
        
        fc = k1/k2**acfinal
        print('Fc = ',fc)
        
        k4 = ((m1*ac1+m2*ac2+m3*ac3)-m2*(ac1+ac2+ac3))/((ac1**2.0)+(ac2**2.0)+(ac3**2.0))-(((ac1+ac2+ac3)**2.0)/3.0)
        print('K4 = ',k4)
        
        k3 = m2 - ((k4*(ac1+ac2+ac3))/3.0)
        print('K3 = ',k3)
        
        m = k3 + k4*acfinal
        print('M = ',m)
        
        a = ((argamassa*(1.0+m))/100.0)-1.0
        print('A = ',a)
        
        p = m - a
        print('P = ',p)
        
        k6 = (1000.0/m3-m1)*((1.0/cimento3)-(1.0/cimento1))
        print('K6 = ',k6)
        
        q = (1000.0/3.0)*((1.0/cimento3)+(1.0/cimento2)+(1.0/cimento1))
        
        k5 = q-k6*m2
        print('K5 = ',k5)
        
        cimento = (1000.0/k5+k6*m)
        
        print('Então: ')
        print('Traço = 1 :',round(a,2),' : ',round(p,2),' : ',round(acfinal,2))        
        


        
    if tipo == 2:
        
        print('Tipo ABCP: ')
        
        abatimento = float(input('Insira o Abatimento: '))
        massaunitariaareia = float(input('Insira a Massa Unitária da Areia: '))
        massaunitariabrita = float(input('Insira a Massa Unitária da Brita: '))
        massaespecificacimento = float(input('Insira a Massa Específica do Cimento: '))
        massaespecificaareia = float(input('Insira a Massa Específica da Areia: '))
        massaespecificabrita = float(input('Insira a Massa Específica da Brita: '))
        dmc = float(input('Insira o DMC da brita: '))
        mf = float(input('Insira o MF da areia: '))
        fck = float(input('Insira o fck: '))
        sd = float(input('Insira o desvio padrão: '))
        
        print('-------'*10)
        
        print('Calculo de Fcd: fcd = fck + 1,65 * sd')
        fcd = fck + 1.65*sd
        print('Fcd =',fcd,' MPa')
        
        print('Calculo de a/c de 28 dias: (92,8 / 7,9^a/c)')
        ac = (math.log(92.8/fcd,10)/math.log(7.9,10))
        print('a/c =',round(ac,2))
        
        ca = 0
        if dmc == 9.5 and abatimento >= 40.0 and abatimento <= 60.0:
                print('O consumo de água é de 220L/m3')
                ca = 220.0             
        elif dmc == 9.5 and abatimento > 60.0 and abatimento <= 80.0:
                print('O consumo de água é de 225L/m3')
                ca = 225.0
        elif dmc == 9.5 and abatimento > 80.0 and abatimento <=100.0:
                print('O consumo de água é de 230L/m3')
                ca = 230.0
        elif dmc == 19.0 and abatimento > 40.0 and abatimento <= 60.0:
                print('O consumo de água é de 195L/m3')
                ca = 195.0
        elif dmc == 19.0 and abatimento > 60.0 and abatimento <=80.0:
                print('O consumo de água é de 200L/m3')
                ca = 200.0
        elif dmc == 19.0 and abatimento > 80.0 and abatimento <= 100.0:
                print('O consumo de água é de 205L/m3')
                ca = 205.0
        elif dmc == 25.0 and abatimento > 40.0 and abatimento <= 60.0:
                print('O consumo de água é de 190L/m3')
                ca = 190.0
        elif dmc == 25.0 and abatimento > 60.0 and abatimento <=80.0:
                print('O consumo de água é de 195L/m3')
                ca = 195.0
        elif dmc == 25.0 and abatimento > 80.0 and abatimento <= 100.0:
                print('O consumo de água é de 200L/m3')
                ca = 200.0
        elif dmc == 32.0 and abatimento > 40.0 and abatimento <= 60.0:
                print('O consumo de água é de 185L/m3')
                ca = 185.0
        elif dmc == 32.0 and abatimento > 60.0 and abatimento <=80.0:
                print('O consumo de água é de 190L/m3')
                ca = 190.0
        elif dmc == 32.0 and abatimento > 80.0 and abatimento <= 100.0:
                print('O consumo de água é de 195L/m3')
                ca = 195.0
        elif dmc == 38.0 and abatimento > 40.0 and abatimento <= 60.0:
                print('O consumo de água é de 180L/m3')
                ca = 180.0
        elif dmc == 38.0 and abatimento > 60.0 and abatimento <=80.0:
                print('O consumo de água é de 185L/m3')
                ca = 185.0
        elif dmc == 38.0 and abatimento > 80.0 and abatimento <= 100.0:
                print('O consumo de água é de 190L/m3')
                ca = 190.0

    consumoCimento = ca/ac
    print('O consumo de cimento será de: ',round(consumoCimento,2),' kg/m3')
                
    if mf == 1.8 and dmc == 9.5:
            print('O Vb é de 0,645kg/m3')
            vb = 0.645
    elif mf == 1.8 and dmc == 19.0:
            print('O vb é de 0,770kg/m3')
            vb = 0.770
    elif mf == 1.8 and dmc == 25.0:
            print('O vb é de 0,795kg/m3')
            vb = 0.795
    elif mf == 1.8 and dmc == 32.0:
            print('O vb é de 0,820kg/m3') 
            vb = 0.820
    elif mf == 1.8 and dmc == 38.0:
            print('O vb é de 0,845kg/m3')   
            vb = 0.845
    elif mf == 2.0 and dmc == 9.5:
            print('O vb é de 0,625kg/m3')
            vb = 0.625
    elif mf == 2.0 and dmc == 19.0:
            print('O vb é de 0,750kg/m3')
            vb = 0.750
    elif mf == 2.0 and dmc == 25.0:
            print('O vb é de 0,775kg/m3') 
            vb = 0.775
    elif mf == 2.0 and dmc == 32.0:
            print('O vb é de 0,800kg/m3')   
            vb = 0.800
    elif mf == 2.0 and dmc == 38.0:
            print('O vb é de 0,825kg/m3')
            vb = 0.825
    elif mf == 2.2 and dmc == 9.5:
            print('O vb é de 0,605kg/m3')
            vb = 0.605
    elif mf == 2.2 and dmc == 19.0:
            print('O vb é de 0,730kg/m3')
            vb = 0.730
    elif mf == 2.2 and dmc == 25.0:
            print('O vb é de 0,755kg/m3') 
            vb = 0.755
    elif mf == 2.2 and dmc == 32.0:
            print('O vb é de 0,780kg/m3')   
            vb = 0.780
    elif mf == 2.2 and dmc == 38.0:
            print('O vb é de 0,805kg/m3')
            vb = 0.805
    elif mf == 2.4 and dmc == 9.5:
            print('O vb é de 0,585kg/m3')
            vb = 0.585
    elif mf == 2.4 and dmc == 19.0:
            print('O vb é de 0,710kg/m3')
            vb = 0.710
    elif mf == 2.4 and dmc == 25.0:
            print('O vb é de 0,735kg/m3') 
            vb = 0.735
    elif mf == 2.4 and dmc == 32.0:
            print('O vb é de 0,760kg/m3')   
            vb = 0.760
    elif mf == 2.4 and dmc == 38.0:
            print('O vb é de 0,785kg/m3')
            vb = 0.785
    elif mf == 2.6 and dmc == 9.5:
            print('O vb é de 0,565kg/m3')
            vb = 0.565
    elif mf == 2.6 and dmc == 19.0:
            print('O vb é de 0,690kg/m3')
            vb = 0.690
    elif mf == 2.6 and dmc == 25.0:
            print('O vb é de 0,715kg/m3') 
            vb = 0.715
    elif mf == 2.6 and dmc == 32.0:
            print('O vb é de 0,740kg/m3')   
            vb = 0.740
    elif mf == 2.6 and dmc == 38.0:
            print('O vb é de 0,765kg/m3')
            vb = 0.765
    elif mf == 2.8 and dmc == 9.5:
            print('O vb é de 0,545kg/m3')
            vb = 0.545
    elif mf == 2.8 and dmc == 19.0:
            print('O vb é de 0,670kg/m3')
            vb = 0.670
    elif mf == 2.8 and dmc == 25.0:
            print('O vb é de 0,695kg/m3') 
            vb = 0.695
    elif mf == 2.8 and dmc == 32.0:
            print('O vb é de 0,720kg/m3')   
            vb = 0.720
    elif mf == 2.8 and dmc == 38.0:
            print('O vb é de 0,745kg/m3')
            vb = 0.745
    elif mf == 3.0 and dmc == 9.5:
            print('O vb é de 0,525kg/m3')
            vb = 0.525
    elif mf == 3.0 and dmc == 19.0:
            print('O vb é de 0,650kg/m3')
            vb = 0.650
    elif mf == 3.0 and dmc == 25.0:
            print('O vb é de 0,675kg/m3') 
            vb = 0.675
    elif mf == 3.0 and dmc == 32.0:
            print('O vb é de 0,700kg/m3')   
            vb = 0.700
    elif mf == 3.0 and dmc == 38.0:
            print('O vb é de 0,725kg/m3')
            vb = 0.725
    elif mf == 3.2 and dmc == 9.5:
            print('O vb é de 0,505kg/m3')
            vb = 0.505
    elif mf == 3.2 and dmc == 19.0:
            print('O vb é de 0,630kg/m3')
            vb = 0.630
    elif mf == 3.2 and dmc == 25.0:
            print('O vb é de 0,655kg/m3') 
            vb = 0.655
    elif mf == 3.2 and dmc == 32.0:
            print('O vb é de 0,680kg/m3')   
            vb = 0.680
    elif mf == 3.2 and dmc == 38.0:
            print('O vb é de 0,705kg/m3')
            vb = 0.705
    elif mf == 3.4 and dmc == 9.5:
            print('O vb é de 0,485kg/m3')
            vb = 0.485
    elif mf == 3.4 and dmc == 19.0:
            print('O vb é de 0,610kg/m3')
            vb = 0.610
    elif mf == 3.4 and dmc == 25.0:
            print('O vb é de 0,635kg/m3') 
            vb = 0.635
    elif mf == 3.4 and dmc == 32.0:
            print('O vb é de 0,660kg/m3')   
            vb = 0.660
    elif mf == 3.4 and dmc == 38.0:
            print('O vb é de 0,685kg/m3')
            vb = 0.685
    elif mf == 3.6 and dmc == 9.5:
            print('O vb é de 0,465kg/m3')
            vb = 0.465
    elif mf == 3.6 and dmc == 19.0:
            print('O vb é de 0,590kg/m3')
            vb = 0.590
    elif mf == 3.6 and dmc == 25.0:
            print('O vb é de 0,615kg/m3') 
            vb = 0.615
    elif mf == 3.6 and dmc == 32.0:
            print('O vb é de 0,640kg/m3')   
            vb = 0.640
    elif mf == 3.6 and dmc == 38.0:
            print('O vb é de 0,665kg/m3')
            vb = 0.665
            
    consumoBrita = vb*massaunitariabrita
    print('O consumo de brita será de: ',round(consumoBrita,2),' kg/m3')      
    
    volumeAreia = 1-((consumoCimento/massaespecificacimento)+(consumoBrita/massaespecificabrita)+(ca/1000))
    
    consumoAreia = volumeAreia*massaespecificaareia
    
    print('O consumo de areia é de: ',round(consumoAreia,2),' kg/m3')
    
    print('Então:\n cimento: ',round(consumoCimento,2),'\n areia: ',round(consumoAreia,2),'\n brita: ',round(consumoBrita,2),'\n agua: ',ca,'\n -----------')
            
    tCimento = consumoCimento/consumoCimento
    tAreia = consumoAreia/consumoCimento
    tBrita = consumoBrita/consumoCimento
    
    print('O traço será de: ',round(tCimento,2),':',round(tAreia,2),':',round(tBrita,2),':',round(ac,2),'com ',round(consumoCimento,2),' kg/m3 de cimento')        
            
            
            
            
else:
        print('numero invalido')
        print('---' * 20)
print('ate mais')