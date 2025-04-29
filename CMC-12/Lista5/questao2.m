function ts = questao2(sys)
% Determinar numericamente o tempo de acomodacao de 2% ts do sistema
% dinamico sys
[~, t1] = step(sys);
limit = t1(end);
t2 = 0:0.001 : limit;
[y,~] = step(sys, t2);
yregime = y(end);
erro = 0.02*yregime;
dentro = abs(y-yregime)<=erro;
for i = 1:length(y)
    if all(dentro(i:end))
        ts = t(i);
    end
end
