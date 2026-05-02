# OPSEC Protocol for SAR Toolkit

## 🔒 General Rules
1. **Never commit PII to version control**: `config/my_details.json` and all files in `responses/` are git-ignored by default.
2. **Run locally only**: Avoid cloud IDEs (GitHub Codespaces, Replit, Google Colab).
3. **Encrypt at rest**: Store the project directory on an encrypted volume (LUKS, FileVault, VeraCrypt).
4. **Secure deletion**: On SSDs/APFS, encryption is more reliable than "secure erase" tools. Delete the encryption key to render data unrecoverable.

## 🛡️ Data Handling

### Personal Data
- **`config/my_details.json`**: Contains PII (name, PPSN, address). **Never share this file.**
- **`responses/`**: Contains SAR responses from agencies. **Treat as highly sensitive.**
- **`output/`**: Contains generated SAR letters. **Sensitive but less so than responses.**

### Forensic Data
- **`forensic/`**: Contains hash indices and chain-of-custody records. **Critical for legal evidence.**
  - Verify hashes regularly using `--verify` mode.
  - Backup this directory separately.

## 🔐 Encryption Recommendations

### Full-Disk Encryption
- **Linux**: LUKS (`cryptsetup`).
- **macOS**: FileVault.
- **Windows**: BitLocker.

### File-Level Encryption
- **GPG**: Encrypt individual files before sharing:
  ```bash
  gpg --symmetric --cipher-algo AES256 --compress-algo 1 --s2k-digest-algo SHA512 config/my_details.json
  ```

## 🚨 Threat Model
| Threat | Mitigation |
|---|---|
| Unauthorized access | Full-disk encryption, strong passwords, lock screen. |
| Data leakage | `.gitignore`, no cloud sync, encrypt backups. |
| File tampering | Forensic hashing (`hash_responses.py`), periodic verification. |
| Metadata leakage | Strip EXIF metadata before sharing images. |
| Shoulder surfing | Privacy screens, avoid public workspaces. |

## 📋 Checklist Before Sharing Files
- [ ] All PII removed or redacted (`redact.py`)?
- [ ] Files hashed and verified?
- [ ] Recipient identity confirmed?
- [ ] Secure transfer method used (encrypted email, Signal)?
- [ ] Chain of custody documented?

## 🛑 What NOT to Do
- ❌ Do not commit `my_details.json` to Git.
- ❌ Do not run scripts in cloud environments.
- ❌ Do not share `responses/` or `forensic/` directories.
- ❌ Do not use weak passwords for encryption.
- ❌ Do not ignore verification failures.
