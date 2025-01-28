import pymysql as My

cn = My.connect(host='localhost', user='root', password='', database='Vacataire')
cr = cn.cursor()

class vacataire:
    def ajouter(self, np: str, e: str, t: int, ap: str, d: str):
        cr.execute(
            "INSERT INTO vacataires (nom_prenom, email, telephone, activite_principale, date_inscription) VALUES (%s, %s, %s, %s, %s)",
            (np, e, t, ap, d),
            )
        cn.commit()

    def modifier(self, np: str, e: str, t: int, ap: str, d: str, i: int):
        cr.execute(
            "UPDATE vacataires SET nom_prenom=%s, email=%s, telephone=%s, activite_principale=%s, date_inscription=%s WHERE idv=%s",
            (np, e, t, ap, d, i),
        )
        cn.commit()

    def supprimer(self, idv: int):
        cr.execute("DELETE FROM vacataires WHERE idv = %s", (idv,))
        cn.commit()

    def afficher_tous(self):
        cr.execute("SELECT * FROM vacataires")
        result = cr.fetchall()
        return result

    def afficher_id(self, idv: int):
        cr.execute("SELECT * FROM vacataires WHERE idv = %s", (idv,))
        result = cr.fetchone()
        return result


class cours:
    def ajouter(self, v: int, m: str, o: str, h: int):
        cr.execute(
            "INSERT INTO cours (vacataire_c, matiere, objectif, heures_prevues) VALUES (%s, %s, %s, %s)",
            (v, m, o, h),
            )
        cn.commit()

    def modifier(self, v: int, m: str, o: str, h: int, i: int):
        cr.execute(
            "UPDATE cours SET vacataire_c=%s, matiere=%s, objectif=%s, heures_prevues=%s WHERE idc=%s",
            (v, m, o, h, i),
        )
        cn.commit()

    def supprimer(self, idc: int):
        cr.execute("DELETE FROM cours WHERE idc = %s", (idc,))
        cn.commit()

    def afficher_tous(self):
        cr.execute(
            "SELECT idc, nom_prenom, matiere, objectif, heures_prevues FROM vacataires v, cours c WHERE c.vacataire_c = v.idv"
        )
        resultat = cr.fetchall()
        return resultat

    def afficher_id_vac(self):
        cr.execute("SELECT idv, nom_prenom FROM vacataires")
        vacataire = cr.fetchall()
        return vacataire


class heure:
    def ajouter(self, v:int, d:str, f:str):
        cr.execute(
            "INSERT INTO heures (vacataire_h, Debut_Travail, Fin_Travail) VALUES (%s, %s,%s)",
            (v, d, f),
            )
        cn.commit()
        
    def modifier(self, v: int, d: str, f: int, i: int):
        cr.execute(
            "UPDATE heures SET vacataire_h=%s, Debut_Travail=%s, Fin_Travail=%s WHERE id=%s",
            (v, d, f, i),
        )
        cn.commit()
        
    def supprimer(self, id: int):
        cr.execute("DELETE FROM heures WHERE id = %s", (id,))
        cn.commit()
    
    def afficher_tous(self):
        cr.execute(
            "SELECT id, nom_prenom, matiere,heures_prevues,Debut_Travail, Fin_Travail FROM vacataires v, cours c, heures h WHERE h.vacataire_h=v.idv and c.vacataire_c=v.idv"
        )
        resultat = cr.fetchall()
        return resultat
    
    def afficher_idh(self, id:int):
        cr.execute("SELECT * FROM Heures WHERE id = %s", (id,))
        resultat = cr.fetchone()
        return resultat
    
    def afficher_vacataires_cours(self):
        cr.execute("SELECT idv,nom_prenom,matiere FROM vacataires v, cours c WHERE c.vacataire_c=v.idv")
        result = cr.fetchall()
        return result
    
class utilisateur:
    def __init__(self, u, m):
        self._u = u  
        self._m = m  

    def authentifier(self):
        cr.execute(
            "SELECT * FROM utilisateurs WHERE username=%s AND password=%s",
            (self._u, self._m),
        )
        d = cr.fetchall()
        if len(d) > 0: 
            if d[0][1] == self._u and d[0][2] == self._m:
                return d  
        return None 