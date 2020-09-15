SET QUOTED_IDENTIFIER OFF 
 SELECT * FROM OPENQUERY(INSQL, "SELECT DateTime = convert(nvarchar, DateTime, 21),Time = convert(char(5), DateTime, 108), [KDCE_GP2_00INS01_00IQWT320.FA_PV0]
 FROM WideHistory 
 WHERE wwRetrievalMode = 'Cyclic' 
 AND wwResolution = 600000 
 AND wwQualityRule = 'Extended' 
 AND wwVersion = 'Latest' 
 AND DateTime >= '20200501 05:00:00.000' 
 AND DateTime <= '20200814 05:00:00.000'") 
 where Time >= '01:00' 
 AND Time <= '05:30'


