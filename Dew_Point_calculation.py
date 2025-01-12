% Enter your MATLAB Code below

readChId = 2805668;
writeChId = 2805701;  % Replace with your channel number

writeKey = '17ESOC5KK41IPBSY';
readKey = 'YQBOZKSPX1DLO93V';

[temp,time] = thingSpeakRead(readChId,'Fields',1,'NumPoints',20);
humidity = thingSpeakRead(readChId,'Fields',2,'NumPoints',20);

tempC = (5/9)*(temp-32); 
b = 17.62;
c = 243.5;
gamma = log(humidity/100) + b*tempC./(c+tempC);
dewPoint = c*gamma./(b-gamma);
dewPointF = (dewPoint*1.8) + 32;

thingSpeakWrite(writeChId,[temp,humidity,dewPointF],'Fields',[1,2,4],...
'TimeStamps',time,'Writekey',writeKey);