from flask import Flask, flash, redirect,url_for,render_template,request,session
from Gestion import vacataire,cours,heure,utilisateur

app=Flask(__name__)
app.secret_key="universiteIslamiqueAuNiger"


@app.route('/')
def index():
    return render_template("login.html")

@app.route('/connecter', methods=['POST'])
def connecter():
    if request.method == 'POST':
        email = request.form['email']
        mot_de_passe = request.form['mot_de_passe']
        user = utilisateur(email, mot_de_passe)
        
        resultat = user.authentifier()
        if resultat: 
            session['utilisateur'] = resultat[0][1]  
            flash("Connexion réussie!", "success")
            return redirect(url_for('vac')) 
        else:
            flash("Email ou mot de passe incorrect!", "danger")
            return redirect(url_for('index'))

@app.route('/deconnecter')
def deconnecter():
    session.pop('utilisateur', None) 
    flash("Vous avez été déconnecté!", "info")
    return redirect(url_for('index'))
#-------------------ZONE VACATAIRE-------------------
@app.route('/vacataire')
def vac():
    if 'utilisateur' in session: 
        a=vacataire().afficher_tous()
        return render_template("Vacataire.html",ar=a)
    else:
        flash("Veuillez vous connecter d'abord!", "warning")
        return redirect(url_for('index'))

@app.route("/ajoutvacataire",methods=['POST','GET'])
def ajoutvacataire():
    if request.method == 'POST':
        ctl=request.form['save']
        n=request.form['nom']
        e=request.form['email']
        t=request.form['tel']
        a=request.form['act']
        d=request.form['date']
        if ctl == 'save':
            vacataire().ajouter(n,e,t,a,d)
        return redirect(url_for('vac'))
    return render_template("Vacataire.html")
@app.route("/modifiervacataire/<int:idv>", methods=['GET', 'POST'])
def modifiervacataire(idv):
    vac_data = vacataire().afficher_id(idv)
    if request.method == 'POST':
        ctl=request.form['modif']
        n = request.form['nom']
        e = request.form['email']
        t = request.form['tel']
        a = request.form['act']
        d = request.form['date']
        if ctl == 'modif':
            vacataire().modifier(n, e, t, a, d, idv)
        # Rediriger vers la page principale des vacataires après modification/Faut suivre pour comprendre
        return redirect(url_for('vac')) 
    # Passer les données du vacataire au template/Quand Monsieur faisait cours vous rigolier non?
    return render_template("Vacataire.html", vacataire=vac_data)

@app.route("/supprimervacataire/<int:idv>", methods=['POST', 'GET'])
def supprimervacataire(idv):
    vacataire().supprimer(idv)
    return redirect(url_for('vac'))

# Fin Ajout Vacataire-----------------------------------------

@app.route("/cours")
def c():
    ce=cours().afficher_id_vac()
    d=cours().afficher_tous()
    return render_template("Cours.html",vacataire=ce,liste=d)
    
@app.route('/ajoutcours', methods=['POST'])
def ajoutcours():
    if request.method == 'POST':
        ctl=request.form['save_c']
        v_c = request.form['vacataire_c']
        m = request.form['matiere']
        o = request.form['objectif']
        h = request.form['heures_prevues']
        if ctl == 'save_c':
            cours().ajouter(v_c,m,o,h)
        return redirect(url_for('c'))
    return render_template("Cours.html")

@app.route('/supprimercours/<int:idc>', methods=['GET'])
def supprimercours(idc):
    cours().supprimer(idc)
    return redirect(url_for('c'))

@app.route('/modifiercours/<int:idc>', methods=['POST'])
def modifiercours(idc):
   # vac_data = cours().afficher_id_vac(idc)
    if request.method == 'POST':
        ctl=request.form['modifier']
        v_c = request.form['vacataire_c']
        m = request.form['matiere']
        o = request.form['objectif']
        h = request.form['heures_prevues']
        if ctl == 'modifier':
            cours().modifier(v_c,m,o,h,idc)
        flash("Cours modifié avec succès", "success")
        return redirect(url_for('c')) 
   # return render_template("Cours.html", vacataire=vac_data)
#---------------Zone Heure------------------------------
@app.route('/heure')
def h():
    vacataires = heure().afficher_vacataires_cours()
    ht=heure().afficher_tous()
    return render_template("Heure.html",heure=vacataires,liste=ht)
    
@app.route('/ajoutheure', methods=['POST'])
def ajoutheure():
    if request.method == 'POST':
        ctl = request.form['save_h']
        v_h = request.form['vacataire_c']  # Récupérer l'ID du vacataire
        debut = request.form['debut']
        fin = request.form['fin']
        if ctl == 'save_h':
            heure().ajouter(v_h, debut, fin)
        return redirect(url_for('h'))
    return render_template("Heure.html")

@app.route('/supprimerheure/<int:id>', methods=['GET'])
def supprimerheure(id):
    heure().supprimer(id)
    return redirect(url_for('h'))


@app.route('/modifier_heure/<int:id>', methods=['POST'])
def modifier_heure(id):
   # vac_data = cours().afficher_id_vac(idc)
    if request.method == 'POST':
        ctl=request.form['modif_h']
        v_h = request.form['vacataire_c']
        debut = request.form['debut']
        fin = request.form['fin']
        if ctl == 'modif_h':
            heure().modifier(v_h,debut,fin,id)
        flash("Modifié avec succèss", "success")
        return redirect(url_for('h')) 

if __name__ == '__main__':
    app.run(host="localhost",port=9999,debug=True)