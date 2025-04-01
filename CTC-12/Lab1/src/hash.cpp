#include "hash.h"

// LOOK FOR THE COMMENTS IN THE .H 
// TO UNDERSTAND WHAT EACH FUNCTION MUST DO

Hash::Hash(int tablesize, int (*hf) (std::string) ) {
    _table.resize(tablesize);
    _hash_func = hf;
}

int Hash::add(std::string str, int &collisions) { 

    if(contains(str, collisions)) return 0;
    else _table[hash(str)].push_front(str);
    
    return 1;

}//add

int Hash::remove(std::string str, int &collisions) { 
    
    int hash_value = hash(str), isThere = 0;

    collisions = 0;

    auto last_it = _table[hash_value].before_begin();
    for(std::string s: _table[hash_value]){
        collisions++;
        if(s==str){
            _table[hash_value].erase_after(last_it);
            isThere = 1;
            break;
        }
        last_it++;
    }
    if(isThere) return 1;

    
    return 0;
    
}//remove


int Hash::hash(std::string str) { 
    
    return _hash_func(str);
    
}//hash
    
int Hash::contains(std::string str, int &collisions) { 
    
    int hash_value = hash(str), isThere = 0;
    
    collisions = 0;

    for(std::string i: _table[hash_value]){
        collisions++;
        if(i==str){
            isThere = 1;
            break;
        }
    }

    return isThere;
    
}//contains


int Hash::worst_case() {

    int worst = 0, siz;

    for(int i=0; i<_table.size(); i++){
        siz = 0;
        for(std::string s: _table[i]) siz++;
        worst = (siz>worst)? siz : worst;
    }

    return worst;
    
}//worst_case

int Hash::size() {

    int siz = 0;

    for(int i=0; i<_table.size(); i++)
        for(std::string s: _table[i]) siz++;

    return siz;

    return 0;
    
}//size

