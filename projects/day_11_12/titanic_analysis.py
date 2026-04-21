"""
============================================================
  COMPREHENSIVE TITANIC DATA ANALYSIS PROJECT
  NumPy + Pandas — Real-World Workflow & Interview Patterns
============================================================

Covers:
  1. Data loading & first-look audit
  2. Missing value analysis & imputation strategies
  3. 8 summary statistics (with reasoning)
  4. Distributions, skewness, kurtosis
  5. Outlier detection (IQR + Z-score)
  6. Correlation analysis (numeric + cramér's V for categorical)
  7. Feature engineering (no loops)
  8. Vectorised ops & broadcasting examples
  9. Linear algebra applications (SVD/PCA, cosine similarity)
  10. Export clean CSV + numerical report
"""

import numpy as np
import pandas as pd
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

SEP = "=" * 60

# ─────────────────────────────────────────────
# 0. HELPERS
# ─────────────────────────────────────────────

def section(title):
    print(f"\n{SEP}")
    print(f"  {title}")
    print(SEP)

def cramers_v(x, y):
    """Cramér's V — association between two categorical variables."""
    ct = pd.crosstab(x, y)
    chi2 = stats.chi2_contingency(ct, correction=False)[0]
    n = ct.sum().sum()
    r, k = ct.shape
    return np.sqrt(chi2 / (n * (min(r, k) - 1)))


# ─────────────────────────────────────────────
# 1. LOAD & FIRST-LOOK AUDIT
# ─────────────────────────────────────────────
section("1. LOAD & FIRST-LOOK AUDIT")

df = pd.read_csv('/home/claude/titanic_raw.csv')

print(f"Shape          : {df.shape}")
print(f"Memory usage   : {df.memory_usage(deep=True).sum() / 1024:.1f} KB")
print(f"\nColumn dtypes:")
print(df.dtypes.to_string())
print(f"\nFirst 3 rows:")
print(df.head(3).to_string())


# ─────────────────────────────────────────────
# 2. MISSING VALUE ANALYSIS
# ─────────────────────────────────────────────
section("2. MISSING VALUE ANALYSIS")

missing = pd.DataFrame({
    'count':   df.isnull().sum(),
    'pct':     (df.isnull().mean() * 100).round(2),
    'dtype':   df.dtypes
}).query('count > 0').sort_values('pct', ascending=False)

print(missing.to_string())

# Strategy matrix
print("\nImputation strategy:")
print("  Age    (19.8%) → median by Pclass+Sex group (preserves distribution shape)")
print("  Cabin  (77.1%) → drop column; >70% missing = uninformative")
print("  Embarked (0.2%)→ mode imputation (near-zero impact)")

# Group-wise median imputation — vectorised, no loops
df['Age'] = df.groupby(['Pclass', 'Sex'])['Age'].transform(
    lambda x: x.fillna(x.median())
)

# Mode imputation for Embarked
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# Drop Cabin
df.drop(columns=['Cabin'], inplace=True)

print(f"\nMissing after imputation: {df.isnull().sum().sum()} values")


# ─────────────────────────────────────────────
# 3. EIGHT SUMMARY STATISTICS
# ─────────────────────────────────────────────
section("3. EIGHT SUMMARY STATISTICS")

numerics = df.select_dtypes(include='number')

# Stat 1: Central tendency
print("\n── Stat 1: Central tendency (mean vs median)")
for col in ['Age', 'Fare', 'SibSp']:
    m, med = numerics[col].mean(), numerics[col].median()
    print(f"  {col:8s}  mean={m:.2f}  median={med:.2f}  "
          f"{'right-skewed' if m > med else 'symmetric'}")

# Stat 2: Dispersion
print("\n── Stat 2: Dispersion (std, IQR, CV)")
for col in ['Age', 'Fare']:
    s = numerics[col]
    cv = s.std() / s.mean() * 100
    iqr = s.quantile(0.75) - s.quantile(0.25)
    print(f"  {col:8s}  std={s.std():.2f}  IQR={iqr:.2f}  CV={cv:.1f}%")

# Stat 3: Skewness
print("\n── Stat 3: Skewness")
skew = numerics.skew().sort_values(ascending=False)
print(skew.round(3).to_string())
print("  (|skew| > 1 = highly skewed; Fare is classic log-normal)")

# Stat 4: Kurtosis
print("\n── Stat 4: Excess kurtosis (> 0 = heavier tails than normal)")
kurt = numerics.kurtosis().sort_values(ascending=False)
print(kurt.round(3).to_string())

# Stat 5: Survival rate
print(f"\n── Stat 5: Overall survival rate: {df['Survived'].mean():.1%}")

# Stat 6: Class distribution
print("\n── Stat 6: Class distribution")
print(df['Pclass'].value_counts(normalize=True).mul(100).round(1).to_string())

# Stat 7: Survival rate by subgroup — vectorised groupby
print("\n── Stat 7: Survival rate by Sex × Pclass (pivot table)")
pivot = df.pivot_table('Survived', index='Sex', columns='Pclass', aggfunc='mean')
print(pivot.round(3).to_string())

# Stat 8: Percentile profile of Fare
print("\n── Stat 8: Fare percentile profile")
pcts = [0, 10, 25, 50, 75, 90, 95, 99, 100]
fare_pcts = np.percentile(df['Fare'], pcts)
for p, v in zip(pcts, fare_pcts):
    print(f"  P{p:3d}: £{v:8.2f}")


# ─────────────────────────────────────────────
# 4. DISTRIBUTION ANALYSIS
# ─────────────────────────────────────────────
section("4. DISTRIBUTION ANALYSIS")

# Normality test (Shapiro-Wilk on sample)
print("Normality tests (Shapiro-Wilk, n=200 sample):")
for col in ['Age', 'Fare']:
    sample = df[col].dropna().sample(200, random_state=42)
    stat, p = stats.shapiro(sample)
    result = "NOT normal" if p < 0.05 else "normal"
    print(f"  {col:8s}: W={stat:.4f}, p={p:.4e} → {result}")

# Log-transform Fare (reduce skew)
df['Fare_log'] = np.log1p(df['Fare'])
print(f"\nFare skewness before log: {df['Fare'].skew():.3f}")
print(f"Fare skewness after log:  {df['Fare_log'].skew():.3f}")

# Age bins — pd.cut (vectorised, no loop)
df['AgeBin'] = pd.cut(df['Age'],
    bins=[0, 12, 18, 35, 60, 100],
    labels=['Child', 'Teen', 'YoungAdult', 'Adult', 'Senior'])

print("\nAge bin distribution:")
print(df['AgeBin'].value_counts().sort_index().to_string())

print("\nSurvival rate by age bin:")
print(df.groupby('AgeBin', observed=True)['Survived'].mean().round(3).to_string())


# ─────────────────────────────────────────────
# 5. OUTLIER DETECTION
# ─────────────────────────────────────────────
section("5. OUTLIER DETECTION")

def detect_outliers_iqr(series, multiplier=1.5):
    """IQR method — robust to skewed distributions."""
    Q1, Q3 = series.quantile([0.25, 0.75])
    IQR = Q3 - Q1
    mask = (series < Q1 - multiplier * IQR) | (series > Q3 + multiplier * IQR)
    return mask

def detect_outliers_zscore(series, threshold=3.0):
    """Z-score method — assumes near-normal distribution."""
    z = np.abs(stats.zscore(series.dropna()))
    return z > threshold

for col in ['Age', 'Fare', 'SibSp', 'Parch']:
    iqr_mask = detect_outliers_iqr(df[col])
    n_outliers = iqr_mask.sum()
    pct = n_outliers / len(df) * 100
    print(f"  {col:8s}: {n_outliers:3d} outliers ({pct:.1f}%) via IQR")

# Multivariate: Mahalanobis distance (NumPy linear algebra)
print("\nMultivariate outliers (Mahalanobis distance):")
num_cols = ['Age', 'Fare', 'SibSp', 'Parch']
X = df[num_cols].dropna().values
X_centered = X - X.mean(axis=0)
cov = np.cov(X.T)
cov_inv = np.linalg.inv(cov)
# Broadcasting: (n, d) @ (d, d) @ (d, n) → vectorised per-row
mahal_sq = np.einsum('ij,jk,ik->i', X_centered, cov_inv, X_centered)
# Chi-squared threshold at 99% with df=4
threshold = stats.chi2.ppf(0.99, df=len(num_cols))
n_multi = (mahal_sq > threshold).sum()
print(f"  {n_multi} multivariate outliers (chi2 threshold @ 99%, df={len(num_cols)})")

# Winsorize Fare at 99th percentile
fare_cap = df['Fare'].quantile(0.99)
df['Fare_winsorized'] = df['Fare'].clip(upper=fare_cap)
print(f"\nFare winsorized at 99th pct (£{fare_cap:.2f})")
print(f"  Max before: £{df['Fare'].max():.2f} → after: £{df['Fare_winsorized'].max():.2f}")


# ─────────────────────────────────────────────
# 6. CORRELATION ANALYSIS
# ─────────────────────────────────────────────
section("6. CORRELATION ANALYSIS")

# Numeric correlations with target
num_df = df[['Survived', 'Pclass', 'Age', 'SibSp', 'Parch', 'Fare']].copy()
corr_matrix = num_df.corr()

print("Correlation with Survived (Pearson r):")
target_corr = corr_matrix['Survived'].drop('Survived').sort_values(key=abs, ascending=False)
for feat, r in target_corr.items():
    bar = '█' * int(abs(r) * 20)
    direction = '+' if r > 0 else '-'
    print(f"  {feat:8s} {direction}{bar:<20s} {r:+.4f}")

# Point-biserial (correct for binary target)
print("\nPoint-biserial correlation (correct for binary Survived):")
for col in ['Age', 'Fare', 'Pclass']:
    valid = df[['Survived', col]].dropna()
    r, p = stats.pointbiserialr(valid['Survived'], valid[col])
    sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "ns"
    print(f"  {col:8s}: r={r:+.4f}  p={p:.4e}  {sig}")

# Cramér's V for categorical features
print("\nCramér's V (categorical association with Survived):")
for col in ['Sex', 'Pclass', 'Embarked', 'AgeBin']:
    v = cramers_v(df['Survived'].astype(str), df[col].astype(str))
    bar = '█' * int(v * 30)
    print(f"  {col:12s} {bar:<30s} V={v:.4f}")

# Multicollinearity check
print("\nHigh correlations among features (|r| > 0.4):")
corr_feat = num_df.drop(columns='Survived').corr()
for i in range(len(corr_feat.columns)):
    for j in range(i+1, len(corr_feat.columns)):
        r = corr_feat.iloc[i, j]
        if abs(r) > 0.4:
            print(f"  {corr_feat.columns[i]} ↔ {corr_feat.columns[j]}: r={r:+.4f}")


# ─────────────────────────────────────────────
# 7. FEATURE ENGINEERING (VECTORISED, NO LOOPS)
# ─────────────────────────────────────────────
section("7. FEATURE ENGINEERING — VECTORISED")

# Title extraction — regex, vectorised
df['Title'] = df['Name'].str.extract(r',\s*([A-Za-z]+)\.', expand=False)
title_map = {
    'Mr': 'Mr', 'Miss': 'Miss', 'Mrs': 'Mrs', 'Master': 'Master',
    'Dr': 'Rare', 'Rev': 'Rare', 'Col': 'Rare', 'Major': 'Rare',
    'Lady': 'Rare', 'Sir': 'Rare'
}
df['Title'] = df['Title'].map(title_map).fillna('Rare')
print("Title distribution:")
print(df['Title'].value_counts().to_string())

# Family features — vectorised arithmetic
df['FamilySize']   = df['SibSp'] + df['Parch'] + 1
df['IsAlone']      = (df['FamilySize'] == 1).astype(int)
df['FamilyGroup']  = pd.cut(df['FamilySize'],
    bins=[0,1,4,11], labels=['Solo','Small','Large'])

# Fare per person (group booking adjustment)
df['FarePerPerson'] = df['Fare'] / df['FamilySize']

# Age × Class interaction (no loop, broadcasting)
df['Age_x_Class'] = df['Age'] * df['Pclass']

# Survival rate by new features
print("\nSurvival by FamilyGroup:")
print(df.groupby('FamilyGroup', observed=True)['Survived'].agg(['mean','count']).round(3).to_string())

print("\nSurvival by Title:")
print(df.groupby('Title')['Survived'].agg(['mean','count']).round(3).to_string())

# One-hot encode categoricals — pd.get_dummies (vectorised)
df_model = df.copy()
df_model = pd.get_dummies(df_model,
    columns=['Sex', 'Embarked', 'Title', 'FamilyGroup'],
    drop_first=False, dtype=int)

# Drop non-model columns
drop_cols = ['PassengerId', 'Name', 'AgeBin']
df_model.drop(columns=[c for c in drop_cols if c in df_model.columns], inplace=True)

print(f"\nModel-ready DataFrame: {df_model.shape}")


# ─────────────────────────────────────────────
# 8. VECTORISED OPS & BROADCASTING SHOWCASE
# ─────────────────────────────────────────────
section("8. VECTORISED OPS & BROADCASTING")

# Z-score normalisation — vectorised, axis-wise
num_features = ['Age', 'Fare', 'SibSp', 'Parch', 'FamilySize', 'FarePerPerson']
X = df[num_features].values
mean = X.mean(axis=0)        # shape (6,)
std  = X.std(axis=0)         # shape (6,)
X_norm = (X - mean) / std    # broadcast: (891,6) - (6,) → works!
print(f"Z-score normalisation:")
print(f"  X shape: {X.shape}  mean shape: {mean.shape}")
print(f"  Mean after norm (should be ~0): {X_norm.mean(axis=0).round(10)}")
print(f"  Std  after norm (should be ~1): {X_norm.std(axis=0).round(3)}")

# Pairwise cosine similarity — broadcasting trick (no loop)
# Compare first 5 passengers' feature vectors
A = X_norm[:5]   # (5, 6)
B = X_norm[:5]   # (5, 6)
A_unit = A / np.linalg.norm(A, axis=1, keepdims=True)  # (5,1) broadcast
B_unit = B / np.linalg.norm(B, axis=1, keepdims=True)
cos_sim = A_unit @ B_unit.T  # (5,5)
print(f"\nPairwise cosine similarity (first 5 passengers):")
print(np.round(cos_sim, 3))

# Softmax on predicted scores — stable version
np.random.seed(0)
logits = np.random.randn(891, 2)  # raw scores for [died, survived]
logits -= logits.max(axis=1, keepdims=True)  # stability
exp_l  = np.exp(logits)
probs  = exp_l / exp_l.sum(axis=1, keepdims=True)
print(f"\nSoftmax probabilities (first 5 passengers):")
print(np.round(probs[:5], 4))
print(f"Row sums (must be 1.0): {probs.sum(axis=1)[:5].round(6)}")


# ─────────────────────────────────────────────
# 9. LINEAR ALGEBRA — SVD / PCA
# ─────────────────────────────────────────────
section("9. LINEAR ALGEBRA — SVD & PCA FROM SCRATCH")

# Full PCA via SVD (no sklearn)
X_c = X_norm - X_norm.mean(axis=0)  # center
U, s, Vt = np.linalg.svd(X_c, full_matrices=False)

# Singular values → explained variance
var_explained = s**2 / np.sum(s**2)
cumvar        = np.cumsum(var_explained)

print("Explained variance per principal component:")
for i, (v, cv) in enumerate(zip(var_explained, cumvar)):
    bar = '█' * int(v * 40)
    print(f"  PC{i+1}: {bar:<40s} {v:.1%}  (cum: {cv:.1%})")

# Project onto top-2 PCs
n_components = 2
X_pca = X_c @ Vt[:n_components].T  # (891, 2)
print(f"\nPCA projection shape: {X_c.shape} → {X_pca.shape}")

# Loadings (feature importance per PC)
loadings = pd.DataFrame(
    Vt[:n_components].T,
    index=num_features,
    columns=[f'PC{i+1}' for i in range(n_components)]
)
print("\nPCA loadings (how each feature contributes):")
print(loadings.round(4).to_string())

# Rank-k approximation error (Eckart–Young theorem)
print("\nRank-k reconstruction error (Frobenius norm):")
for k in [1, 2, 3, 6]:
    X_approx = U[:, :k] * s[:k] @ Vt[:k, :]
    err = np.linalg.norm(X_c - X_approx, 'fro')
    print(f"  k={k}: ||error||_F = {err:.4f}  "
          f"(variance retained: {cumvar[k-1]:.1%})")

# Condition number — numerical stability indicator
cond = np.linalg.cond(X_norm)
print(f"\nCondition number of feature matrix: {cond:.2f}")
print(f"  (< 100 = well-conditioned, fine for linear models)")

# Matrix norm
print(f"Frobenius norm of X_norm: {np.linalg.norm(X_norm, 'fro'):.4f}")
print(f"Spectral norm (largest singular value): {s[0]:.4f}")


# ─────────────────────────────────────────────
# 10. EXPORT
# ─────────────────────────────────────────────
section("10. EXPORT CLEAN CSV & SUMMARY REPORT")

# Clean export
clean_cols = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age',
              'SibSp', 'Parch', 'Fare', 'Embarked',
              'Title', 'FamilySize', 'IsAlone', 'FamilyGroup',
              'FarePerPerson', 'Fare_log', 'Age_x_Class', 'AgeBin']
df_clean = df[[c for c in clean_cols if c in df.columns]]
df_clean.to_csv('/home/claude/titanic_clean.csv', index=False)
print(f"Clean CSV saved: titanic_clean.csv  {df_clean.shape}")

# Numerical summary report
report_lines = [
    "TITANIC DATA ANALYSIS — SUMMARY REPORT",
    "=" * 50,
    f"Passengers analysed : {len(df):,}",
    f"Features (raw)      : 11",
    f"Features (engineered): {len(df_clean.columns)}",
    "",
    "── MISSING VALUES ──",
    f"  Age imputed   : {df['Age'].isnull().sum()} rows (group median)",
    f"  Cabin dropped : 686 rows (77.1% missing)",
    f"  Embarked filled: 2 rows (mode)",
    "",
    "── KEY STATISTICS ──",
    f"  Overall survival   : {df['Survived'].mean():.1%}",
    f"  Female survival    : {df[df.Sex=='female']['Survived'].mean():.1%}",
    f"  Male survival      : {df[df.Sex=='male']['Survived'].mean():.1%}",
    f"  1st class survival : {df[df.Pclass==1]['Survived'].mean():.1%}",
    f"  3rd class survival : {df[df.Pclass==3]['Survived'].mean():.1%}",
    f"  Median age         : {df['Age'].median():.1f} yrs",
    f"  Median fare        : £{df['Fare'].median():.2f}",
    f"  Solo travellers    : {df['IsAlone'].mean():.1%}",
    "",
    "── CORRELATIONS WITH SURVIVAL ──",
    f"  Sex (Cramér's V)   : {cramers_v(df['Survived'].astype(str), df['Sex']):.4f}  [strongest]",
    f"  Pclass (Cramér's V): {cramers_v(df['Survived'].astype(str), df['Pclass'].astype(str)):.4f}",
    f"  Fare (Pearson r)   : {df['Survived'].corr(df['Fare']):+.4f}",
    f"  Age  (Pearson r)   : {df['Survived'].corr(df['Age']):+.4f}",
    "",
    "── PCA SUMMARY ──",
    f"  PC1 explains       : {var_explained[0]:.1%} of variance",
    f"  PC2 explains       : {var_explained[1]:.1%} of variance",
    f"  Top-2 PCs total    : {cumvar[1]:.1%} of variance",
    "",
    "── OUTLIERS ──",
    f"  Fare (IQR)         : {detect_outliers_iqr(df['Fare']).sum()} outliers ({detect_outliers_iqr(df['Fare']).mean():.1%})",
    f"  Fare winsorized at : £{fare_cap:.2f} (99th pct)",
    f"  Multivariate (Mahalanobis): {n_multi} outliers",
]

report = "\n".join(report_lines)
print(report)

with open('/home/claude/analysis_report.txt', 'w') as f:
    f.write(report)

print("\n✓ analysis_report.txt saved")
print("✓ titanic_clean.csv saved")
print("\nAll done — comprehensive analysis complete.")
