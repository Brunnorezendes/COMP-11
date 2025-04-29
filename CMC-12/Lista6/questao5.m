function [Kp, Ki] = questao5()
% Considerando um circuito RC com R = 10 kOhm e C = 1 muF, calcule ganhos
% Kp e Ki de um controlador PI com pre-filtro para que o sistema tenha
% tempo de subidade de 0 a 100% tr = 0.01 s e sobressinal Mp = 0.046.

% Kp = ...
% Ki = ...

tr = 0.01;
Mp = 0.046;
R = 10000;
C = 0.000001;

xi = -log(Mp)/sqrt(pi.^2 + log(Mp).^2);
wn = (pi-acos(xi))/(tr*sqrt(1-xi.^2));

Ki = R*wn.^2;
Kp = 2*xi*wn*R - C;

end
