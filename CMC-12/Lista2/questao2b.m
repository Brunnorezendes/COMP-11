function omegaInf = questao2b()
% Retorne a velocidade do motor em regime, considerando os parametros
% do motor Maxon RE-max 17 214897. Use SI.

% omegaInf = ...
V = 14.8;
b = 8.87*10^(-8);
Kt = 10.7*10^(-3);
R = 8.3;
omegaInf = V*Kt/(b.*R + Kt^2);

end