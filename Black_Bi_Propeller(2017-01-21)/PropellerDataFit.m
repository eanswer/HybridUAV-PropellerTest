clear all; close all; clc;

result = dlmread('Black_Bi_Propeller_Test.txt');
pwm = result(:,1);
Voltage = result(:,4);
Thrust = result(:,3);
Torque = result(:,2);

meanVoltage = mean(Voltage);
stdVoltage = std(Voltage);
meanPwm = mean(pwm);
stdPwm = std(pwm);
Voltage = (Voltage - meanVoltage) / stdVoltage;
pwm = (pwm - meanPwm) / stdPwm;


figure
sf = fit([pwm, Voltage], Thrust,'poly21')
plot(sf, [pwm, Voltage], Thrust);


figure
f = fit(Thrust, Torque, 'poly1')
plot(f, Thrust, Torque)

