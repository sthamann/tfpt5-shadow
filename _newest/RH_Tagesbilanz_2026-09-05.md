# RH-Programm – Tagesbilanz 5. September 2026

Claim boundary: Forschungsprotokoll; kein Beweis und kein Gegenbeweis der
Riemannschen Vermutung.

## Ergebnis des All-Place-/Tate-Audits

Die erneute Prüfung von Calabi--Yau-Geometrie, Tate-Faktoren, Code- und
Quantenstrukturen hat die Restlücke enger gemacht, aber nicht geschlossen:

- Der starre Level-8-Calabi--Yau-Kanal isoliert den skalaren Zeta-Faktor exakt über
  \(\operatorname{End}(H^3)=\mathbf Q(0)\oplus\operatorname{Ad}^0(H^3)\).
- Der Tate-Projektor \(A\mapsto\operatorname{tr}(A)I/2\) ist exakt, equivariant und
  selbstadjungiert. Auch bei \(p=2\) bleibt die Identitätslinie inertiafest.
- Die Vervollständigung muss den Polfaktor behalten:
  \(\Lambda_{\mathbf Q}(u)=2\xi(u)/(u(u-1))\), nicht einfach \(\xi(u)\).
- Der richtige Symmetric-square-Primkoeffizient ist \(a_p^2-p^3\); die ältere
  Beschriftung \(a_p^2-2p^3\) ließ den mittleren Eigenwert \(p^3\) aus.
- Das skalare Bild der Tate-Projektion enthält keine Level-8-, \(f_8\)-,
  Calabi--Yau- oder \(E_8/H_8\)-spezifische Information. Soweit projektive
  Darstellungsdaten in \(\operatorname{End}(H^3)\) überleben, liegen sie im
  Adjoint-Anteil; Twist-, Vorzeichen- und Realisierungsdaten können ganz verloren gehen.
  Der Projektor identifiziert den Faktor, erzeugt aber keine neue Zeta-Positivität.

## Neuer No-go für feste endliche Träger

Eine lineare Abbildung aus dem unendlichdimensionalen Weil-Testfunktionsraum in einen
festen endlichdimensionalen Hodge-, Code-, Calabi--Yau- oder Quantenraum besitzt einen
Kernel. Jede von einer positiven Form auf diesem endlichen Raum zurückgezogene Form
verschwindet dort.

Zusammen mit der im externen v2-Preprint von Zhu zertifizierten strikten Fensterpositivität auf
\([-0.8,0.8]\) folgt: Kein fester endlicher linearer \(E_8\)-, \(H_8\)-,
\(H^3\)- oder \(\operatorname{End}(H^3)\)-Träger kann die vollständige Weil-Form auf
diesem Fenster als exakter linearer Pullback sein. Das schließt nichtlineare Verfahren,
wachsende endliche Diskretisierungen, direkte Limiten oder unendliche
adelische/operatoralgebraische Realisierungen nicht aus.

## Korrektur des historischen T49-Rankin-Laufs

Der frühere Schluss

\[
\sum_{n\le X}b_n=O(X^q),\quad b_n\ge0
\quad\Longrightarrow\quad
b_n=O(n^{q-1+\varepsilon})
\]

ist falsch. Die auf demselben endlichen Fenster definierte
Maximalkonstante \(K\) machte den anschließenden Test tautologisch.

Das exakte Gegenbeispiel

\[
b_n=4n^3+\mathbf 1_{\{n=32^m\}}n^{18/5}
\]

behält \(A(X)\sim X^4\) und den einfachen Dirichletreihenpol bei \(s=4\), verletzt aber
entlang der Spikes jede \(O(n^{31/10})\)-Schranke. Die Tau-Variante funktioniert mit
Grundterm \(12n^{11}\) und Spike-Exponent \(58/5\).

Rankins tatsächlicher Schluss von 1939 benutzt einen quantitativen Fehlerterm der
Rankin--Selberg-Asymptotik; ein Pol und Nichtnegativität allein genügen nicht. Die
gültigen Jacobi-, Hecke- und Rankin--Selberg-Identitäten der historischen Probe bleiben
erhalten. Ihr aktuelles Verdict ist:

    RANKIN-EXPONENT-DROP-FALSIFIED; FINITE-IDENTITIES-SURVIVE

## Reproduzierbare Repo-Artefakte

- verification/v1021_all_place_tate_rank_audit.py – 23 exakte Checks.
- experiments/tfpt-discovery/rankin_positivity_miniature_probe.py – ausführbare
  Correction of Record, 30 Checks.
- rh/catalog/analysis/all_place_tate_audit.md und .json – vollständige Typisierung.
- rh/catalog/fragments/part_19.json – kuratierte Katalogkorrektur.
- Konzeptkarte – neue Knoten für Tate-Projektor, Informationsverlust,
  das exakte Rang-Nullitäts-Lemma, die getrennt als externe Preprint-Prämisse typisierte
  strikte Fenster-Floor-Aussage, absolute Twistor-Linie, Petz--Watatani--Tate-Netz und
  die offene Tate--Weil-Realisierung.

## Der vollständige Restvertrag

Eine wirkliche Lösung braucht weiterhin alle sieben Teile:

1. eine absolute Kurve mit allen endlichen Stellen, \(\infty\), Skalenaktion und \(p=2\);
2. ihr all-place Quadrat mit wohldefiniertem Arakelov-Schnitt;
3. einen linearen, injektiven, stetigen Compiler \(f\mapsto D_f\) mit
   unendlichdimensionalem Bild oder eine kompatible unbeschränkte/direct-limit Familie;
4. eine exakte lokale Schnittidentität für Primzahlpotenzen, Gamma-, \(\log\pi\)- und
   Polterm;
5. einen unabhängig bewiesenen absoluten Hodge-Index auf dem gesamten Bild;
6. den Dichte-, Abschluss- und Konvergenzübergang zur vollen Weil-Testklasse;
7. eine globale regularisierte Trace-/Determinantenidentität mit allen lokalen
   Normalisierungen.

Der erste echte neue Satz wäre die **Tate--Weil-Realisierung**: eine
nullstellenunabhängige all-place Korrespondenzfamilie \(D_f\), deren Schnittpaarung exakt
die polarisierte Weil-Form ist. Danach fehlt noch der absolute Hodge-Index. Weder
endliche Code-/Quantenpositivität noch die bloße Tate-Faktorisierung liefern diese
beiden Sätze.

## Stand in einem Satz

Der Zeta-Faktor ist jetzt lokal und motivisch sauber isoliert. Zwei Abkürzungen sind
präzise begrenzt: Ein fester endlicher Träger kann den vollen strikt positiven
Fensterraum nicht exakt linear tragen (bedingt auf die externe Floor-Prämisse), und der
Rankin-Mittelwertsprung ist falsch. Offen bleibt für die untersuchte geometrische Route
das globale all-place Objekt samt unabhängiger Schnittpositivität. Kein RH-Claim.
