# Source-defect adjudication

Four original-print-confirmed R823 defects are corrected in the English target
and disclosed immediately there:

1. `N04-S08-SRCDEF-001`, R823 line 4442: the editable source splits the
   printed closed compound *Schlussform*. The English reads "final form."
2. `N04-S08-SRCDEF-002`, R823 line 4475: the editable source splits the
   printed closed compound *Schlussausdruecke*. The English reads "final
   expressions."
3. `N04-S08-SRCDEF-003`, R823 line 4457: the editable source makes the first
   dual sequence descend. The print has the ascending range
   `T^(rho+1), ..., T^(rho+lambda-1)`. Only this first sequence is restored;
   the second remains descending as printed.
4. `N04-S08-SRCDEF-004`, R823 line 4348: the editable source has
   *mit der beiden Reihen*; the print has the dative plural
   *mit den beiden Reihen*. The English reads "with the two rows."

The three upstream correction receipts are external evidence, not missing
package artifacts:

- lexical defects 001-002: 2,261 bytes, SHA-256
  `9505D6A1724936E8D0DA968172AB88E50003BF082816C66DCEB12EED5F0CA477`;
- formula defect 003: 3,487 bytes, SHA-256
  `6BEAE2793DEA5AA477D3E3F74DB108D386C2C9483BE228269A0F83BC9534FD09`;
- grammatical defect 004: 2,349 bytes, SHA-256
  `440FB6092695D0BE79088C7BD18BB76348BD45CD6B45EC8577E8A5F99D2A5B01`.

Their internal-routing filenames and bodies are intentionally excluded. The
public source-control ledger and evidence graph use typed external-alert
receipts and retain the defect IDs, evidence hashes, scopes, and dispositions.
