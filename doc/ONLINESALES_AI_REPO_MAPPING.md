# OnlineSales.ai Repository Mapping and Organization Settings

This document consolidates the repository ownership mapping across the organization, generated directly from the latest Access tables.
> **Note:** This list specifically filters out `read`-only access and generic org-wide teams (like `dev`) to establish true ownership. It also standardizes team names (e.g. `ui-write` becomes `ui`).

## Organization Settings Changes
To enforce the governance model, the following configurations will be centrally applied at the GitHub Organization level:

### 1. Custom Properties (Repository Metadata)
- **Property Created:** A new custom property named `Team` (Type: `Multi Select`) will be generated at the Org level.
- **Assignment:** The automated scripts will loop through the table below and tag each repository with its corresponding `Team` property, definitively establishing ownership.

### 2. Organization Ruleset (Branch Protection & Approvals)
An Organization-level Repository Ruleset named **"Enforce Standard Branch Flows"** will be deployed, targeting all repositories (`~ALL`), to enforce the following:
- **Protected Branches:** Applies to `stage`, `release`, `main`, and `master`.
- **Mandatory PR & Approvals:** Direct pushes to these branches are blocked. All changes must go through a Pull Request and receive a minimum of **2 Approving Reviews** before merging.
- **Strict Pipeline Flow (`feature` -> `stage` -> `release`/`main`):** Pull Requests targeting `release`, `main`, or `master` will rigidly require the source branch to be exactly `stage`. Pull Requests targeting `stage` cannot originate from `release`, `main`, or `master`. Any feature branch can be merged to `stage`.
- **Bypass Privileges:** Only users with `OrganizationAdmin` privileges can bypass these restrictions in case of an emergency.

---

**Distinct Teams Found:**
- `cw-python`
- `cw-qa`
- `flairminds`
- `frigga-cloud`
- `hyperlocal`
- `hyperlocal-performance`
- `infra`
- `instore`
- `osmos-client-delight`
- `osmos-data`
- `osmos-media`
- `osmos-offsite`
- `osmos-performance`
- `osmos-qa`
- `osmos-rms`
- `osmos-rms-ui`
- `osmos-sdk`
- `osmos-ui`
- `osmso-offsite`
- `retailium`
- `ui`
- `ui-team`

| Repository Name | Assigned Team | Access Role | Check |
| :--- | :--- | :--- | :---: |
| `GithubOrgPoliciesRestriction` | infra | admin | [ ] |
| `demo-repository` | ui | admin | [ ] |
| `onlinesales-ai/AdServerESOConfiguration` | osmos-client-delight | admin | [ ] |
| `onlinesales-ai/ArgoCD-Adserver` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/ArgoCD-Prod` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/ArgoCD-Stage` | frigga-cloud, infra, osmos-client-delight | admin | [ ] |
| `onlinesales-ai/InstoreDigitalScreenStatusSync` | instore | admin, write | [ ] |
| `onlinesales-ai/OS-Debezium` | infra | admin | [ ] |
| `onlinesales-ai/UUIDGenerator` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/acquire-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/ad-server-test` | osmos-media | admin, write | [ ] |
| `onlinesales-ai/ad-sim` | ui | admin, write | [ ] |
| `onlinesales-ai/adServer-frigga` | frigga-cloud, infra | maintain | [ ] |
| `onlinesales-ai/addToWorkloadIdentity` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/admin-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/adrequest-debugger` | osmos-client-delight | write | [ ] |
| `onlinesales-ai/adserver-deployment-monitoring` | osmos-performance | write | [ ] |
| `onlinesales-ai/adserver-setup-terraform` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/android-os-sdk` | osmos-client-delight, osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/android-osmos-sdk-source` | osmos-client-delight, osmos-sdk | admin, maintain, write | [ ] |
| `onlinesales-ai/aresJobGen` | hyperlocal, osmos-client-delight, osmos-data, osmos-media, osmos-offsite, osmos-performance, osmos-rms, osmos-rms-ui | admin, write | [ ] |
| `onlinesales-ai/argocd-management-cluster` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/argocd-terraform` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/argocd-test-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/asyncJobsService` | frigga-cloud, infra, osmos-performance, osmos-rms | admin, maintain, write | [ ] |
| `onlinesales-ai/athenaJobsV4BQ` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/athenaJobsV5` | frigga-cloud | write | [ ] |
| `onlinesales-ai/audience-segment-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/audit-service-api-qa` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/auditConsumer` | osmos-rms | write | [ ] |
| `onlinesales-ai/auditService` | frigga-cloud, osmos-rms, osmos-rms-ui | admin, triage, write | [ ] |
| `onlinesales-ai/authentication4node` | frigga-cloud | write | [ ] |
| `onlinesales-ai/beamEventProcessor` | osmos-media | write | [ ] |
| `onlinesales-ai/brand-ads-ui-service-api-qa` | osmos-rms-ui | write | [ ] |
| `onlinesales-ai/brandAdServerV2` | frigga-cloud, infra, osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/brandAdServerV2-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/brandAdsUIService` | frigga-cloud, infra, osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/brandads-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/budgetEngine` | frigga-cloud, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/bulk-actions` | ui | admin, write | [ ] |
| `onlinesales-ai/butlerService` | frigga-cloud, hyperlocal, infra, osmos-performance, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/cacheLib` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/cacheLib_frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/campaignCloner` | osmos-media | maintain | [ ] |
| `onlinesales-ai/campaignUserActionConsumer` | osmos-client-delight, osmos-media | admin, maintain, write | [ ] |
| `onlinesales-ai/campaign_debugger_agent` | osmos-data, osmos-media | write | [ ] |
| `onlinesales-ai/captain-js` | ui | admin, write | [ ] |
| `onlinesales-ai/catalogSyncService` | frigga-cloud, osmos-client-delight, osmos-rms, osmos-rms-ui | admin, maintain, write | [ ] |
| `onlinesales-ai/chrome-extension-icon-changer` | ui | admin, write | [ ] |
| `onlinesales-ai/cis-ui` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/comment-service-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/craftService` | frigga-cloud, infra, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/creativeUploadService` | osmos-client-delight | write | [ ] |
| `onlinesales-ai/dataValidationExecutorV2` | osmos-data | admin, write | [ ] |
| `onlinesales-ai/dataflow-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/datasync-shared-config` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/dblib` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/demo-java-app` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/demo-mobile-apps` | osmos-client-delight, osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/devOpsTools` | flairminds | write | [ ] |
| `onlinesales-ai/developers-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/documentation` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/domain-config-updator` | ui | admin, write | [ ] |
| `onlinesales-ai/ds-opc-classification-prediction` | osmos-performance | write | [ ] |
| `onlinesales-ai/ds-opc-classification-training` | osmos-performance | admin, write | [ ] |
| `onlinesales-ai/ds-search-relevancy-repo` | osmos-performance | admin, write | [ ] |
| `onlinesales-ai/ds-sku-sku-relevancy-prediction` | osmos-performance | admin, write | [ ] |
| `onlinesales-ai/ds-sku-sku-relevancy-training` | osmos-performance | admin, write | [ ] |
| `onlinesales-ai/ds-sku-sku-relevancy-v3` | osmos-performance | admin, write | [ ] |
| `onlinesales-ai/engageService` | frigga-cloud, infra, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/engageService-api-qa` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/engageServiceConsumer` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/experimentalCacheScripts` | osmos-performance | maintain | [ ] |
| `onlinesales-ai/fileBasedAudienceSync` | osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/financeService` | frigga-cloud, osmos-client-delight, osmos-offsite, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/financeServiceConsumer_deprecated` | osmos-client-delight, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/flairminds` | flairminds, hyperlocal, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/flexi-packages-ui-automation-qa` | cw-qa | write | [ ] |
| `onlinesales-ai/flutter-ecommerce-demo-app` | osmos-client-delight | admin | [ ] |
| `onlinesales-ai/flutter-os-sdk` | osmos-client-delight, osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/flutter-osmos-sdk-source` | osmos-client-delight, osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/frigga-engageService` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/frigga-testing-daemon` | frigga-cloud, infra | maintain, write | [ ] |
| `onlinesales-ai/gcp-alerts-terraform` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/gcp-infra` | frigga-cloud, infra | admin | [ ] |
| `onlinesales-ai/gitops` | flairminds, infra | admin, write | [ ] |
| `onlinesales-ai/gradle-wrapper` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/hadesObjects` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/hadesV2` | frigga-cloud | write | [ ] |
| `onlinesales-ai/hotstarSharedLib` | frigga-cloud | write | [ ] |
| `onlinesales-ai/httpRequest` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/hyperlocal-admin-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-maverick-ui` | osmos-ui, ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-microsite-monitor` | ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-microsites` | ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-microsites-strapi` | ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-partner-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-pulse-ui` | osmos-ui, ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-shared-ui` | osmos-ui, ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-shared-ui-v2` | osmos-ui, ui | admin, write | [ ] |
| `onlinesales-ai/hyperlocal-ui-qa` | ui | write | [ ] |
| `onlinesales-ai/hyperlocalCampaignConfidenceScorePopulator` | frigga-cloud, hyperlocal | write | [ ] |
| `onlinesales-ai/hyperlocalForecastingModelTrainingFlow` | frigga-cloud, hyperlocal | write | [ ] |
| `onlinesales-ai/iab-url-verification` | osmos-client-delight, ui | admin, write | [ ] |
| `onlinesales-ai/in-store-screen-registration-API` | instore | write | [ ] |
| `onlinesales-ai/in-store-web-player` | ui | admin, write | [ ] |
| `onlinesales-ai/instore-cms-client` | infra, instore | admin, write | [ ] |
| `onlinesales-ai/instoreAdServer` | frigga-cloud, instore | admin, write | [ ] |
| `onlinesales-ai/instoreAlerting` | instore | admin, write | [ ] |
| `onlinesales-ai/instoreCMSSync` | frigga-cloud, instore | admin, write | [ ] |
| `onlinesales-ai/instoreCampaignBookingProcessor` | instore | admin, write | [ ] |
| `onlinesales-ai/instoreConsumer` | instore | admin, write | [ ] |
| `onlinesales-ai/instoreRedisLoader` | infra, instore | admin, write | [ ] |
| `onlinesales-ai/instoreSchedulingConsumer` | frigga-cloud, infra, instore | admin, write | [ ] |
| `onlinesales-ai/instoreScripts` | infra, instore | admin, write | [ ] |
| `onlinesales-ai/instoreService` | frigga-cloud, infra, instore | admin, write | [ ] |
| `onlinesales-ai/instoreTranscoder` | instore | admin, write | [ ] |
| `onlinesales-ai/ios-os-sdk` | osmos-client-delight, osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/ios-osmos-sdk-source` | osmos-client-delight, osmos-sdk | admin, maintain, write | [ ] |
| `onlinesales-ai/java-daemon-app-template` | frigga-cloud | write | [ ] |
| `onlinesales-ai/java-offline-app-template` | frigga-cloud | write | [ ] |
| `onlinesales-ai/java-shared-lib-template` | frigga-cloud, infra | maintain, write | [ ] |
| `onlinesales-ai/java-tomcat-app-template` | frigga-cloud | write | [ ] |
| `onlinesales-ai/jobWrapper` | frigga-cloud | write | [ ] |
| `onlinesales-ai/kam-service-api-qa` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/kamService` | frigga-cloud, hyperlocal, instore, osmos-client-delight, osmos-data, osmos-performance, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/keywordTargetingService-api-qa` | osmos-client-delight, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/kuber-service-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/kuberService` | frigga-cloud, osmos-client-delight, osmos-rms, retailium | admin, write | [ ] |
| `onlinesales-ai/labs` | hyperlocal | admin, write | [ ] |
| `onlinesales-ai/launcherSharedLib` | osmos-offsite, osmso-offsite | write | [ ] |
| `onlinesales-ai/live-ads-plugin` | ui | write | [ ] |
| `onlinesales-ai/lmsCrmSyncApp` | frigga-cloud, hyperlocal | admin, write | [ ] |
| `onlinesales-ai/lmsNodeEventManagerConsumer` | frigga-cloud, hyperlocal, infra | admin, write | [ ] |
| `onlinesales-ai/localium-DA-Meta-workspace` | hyperlocal-performance | write | [ ] |
| `onlinesales-ai/localium-DA-workspace` | hyperlocal-performance | write | [ ] |
| `onlinesales-ai/localium-catalog-svc` | frigga-cloud, hyperlocal, osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/logger` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/logger_frigga` | frigga-cloud, infra | admin | [ ] |
| `onlinesales-ai/marketing-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/marketingService` | frigga-cloud, osmos-client-delight, osmos-media, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/marketingServiceConsumer` | osmos-media | admin, write | [ ] |
| `onlinesales-ai/marketplaceBillingApplication` | osmos-media | admin, write | [ ] |
| `onlinesales-ai/maverick-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/mediaPythonScripts` | osmos-client-delight, osmos-data, osmos-media, osmos-performance, osmos-rms | admin, maintain, write | [ ] |
| `onlinesales-ai/mediaRubyScripts` | osmos-client-delight, osmos-media | admin, maintain, write | [ ] |
| `onlinesales-ai/molocoSharedLib` | frigga-cloud | write | [ ] |
| `onlinesales-ai/multiVerseService` | frigga-cloud, infra, osmos-rms, osmos-rms-ui, ui | admin, write | [ ] |
| `onlinesales-ai/navigatorService` | frigga-cloud, instore, osmos-client-delight, osmos-data, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/novuWorkflows` | frigga-cloud, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/offerService` | frigga-cloud, osmos-client-delight, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/offsiteReportProject` | osmos-offsite | write | [ ] |
| `onlinesales-ai/onboarding-service-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/onboardingScripts` | hyperlocal, infra, instore, osmos-client-delight, osmos-data, osmos-media, osmos-offsite, osmos-performance, osmos-rms, osmos-rms-ui | admin, write | [ ] |
| `onlinesales-ai/os-2c2p-client` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/os-adserver-util` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/os-bullmq` | osmos-rms | write | [ ] |
| `onlinesales-ai/os-bullmq-client` | instore | write | [ ] |
| `onlinesales-ai/os-client-tracker` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/os-cms` | osmos-rms, ui | admin, write | [ ] |
| `onlinesales-ai/os-common-middlewares` | frigga-cloud, osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/os-gcp-client` | osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/os-infra-terraform` | frigga-cloud | write | [ ] |
| `onlinesales-ai/os-moloco-client` | osmos-client-delight | admin | [ ] |
| `onlinesales-ai/os-pay-pal-ad-server-setup-terraform` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/os-pay-pal-vpc-setup-terraform` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/os-pyutils` | frigga-cloud, instore, osmos-client-delight, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/os-pyutils-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/os-svc-client` | osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/os-terraform` | frigga-cloud, infra | admin | [ ] |
| `onlinesales-ai/os-terraform-vpc` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/os-ui-doc` | ui | admin, write | [ ] |
| `onlinesales-ai/osAdServerConfigs` | infra | admin | [ ] |
| `onlinesales-ai/osAdsAudienceRedisPusherApp` | frigga-cloud, osmos-client-delight, osmos-media | admin, write | [ ] |
| `onlinesales-ai/osAdsTargetingProcessorApp` | frigga-cloud, osmos-client-delight, osmos-media | admin, write | [ ] |
| `onlinesales-ai/osAudienceUpdator` | osmos-client-delight, osmos-media, osmos-offsite, osmos-rms | admin, maintain | [ ] |
| `onlinesales-ai/osFacebookClient` | frigga-cloud, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/osFileStreamProcessorApp` | cw-python, frigga-cloud, osmos-client-delight, osmos-media, osmos-performance, osmos-rms | admin, maintain, write | [ ] |
| `onlinesales-ai/osGoogleAdsClient` | frigga-cloud | write | [ ] |
| `onlinesales-ai/osPackageLauncher` | frigga-cloud, infra, osmos-client-delight, osmos-rms, osmos-rms-ui | admin, maintain, write | [ ] |
| `onlinesales-ai/osPackageSvc` | frigga-cloud, osmos-client-delight, osmos-media, osmos-rms | admin, maintain, write | [ ] |
| `onlinesales-ai/osPackageSvcConsumer` | osmos-rms | write | [ ] |
| `onlinesales-ai/osSchedulesArgoSyncer` | frigga-cloud | write | [ ] |
| `onlinesales-ai/osSolrLoaderApp` | osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/osSvcClient4pyV2` | cw-python, frigga-cloud, infra, osmos-client-delight, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/osSvcClient4pyV2-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/osTemporalClient` | osmos-offsite | write | [ ] |
| `onlinesales-ai/osTiktokAdsClient` | frigga-cloud, osmos-offsite | write | [ ] |
| `onlinesales-ai/osmos-advertiser-suggestion-generator` | frigga-cloud, infra, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/osmos-api-qa` | osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/osmos-claude-plugins` | instore, osmos-data | write | [ ] |
| `onlinesales-ai/osmos-data-analysis-agent` | osmos-performance | write | [ ] |
| `onlinesales-ai/osmos-display-adserver-api-qa` | osmos-client-delight, osmos-media, osmos-performance | admin, maintain, write | [ ] |
| `onlinesales-ai/osmos-events-api-qa` | osmos-media | write | [ ] |
| `onlinesales-ai/osmos-flutter-sdk` | osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/osmos-icu-tokenizer` | frigga-cloud, infra, osmos-client-delight | admin, maintain, write | [ ] |
| `onlinesales-ai/osmos-iframe-sdk` | osmos-rms-ui, ui | admin, write | [ ] |
| `onlinesales-ai/osmos-inference-svc` | frigga-cloud, osmos-performance | admin, maintain, write | [ ] |
| `onlinesales-ai/osmos-keyword-curator-app` | frigga-cloud, infra, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/osmos-lead-form` | ui | admin, write | [ ] |
| `onlinesales-ai/osmos-perf-irrelevancy-identification` | osmos-performance | write | [ ] |
| `onlinesales-ai/osmos-pla-auto-keyword-targeting-bid-optimizer` | osmos-performance | write | [ ] |
| `onlinesales-ai/osmos-pulse-qa` | ui | write | [ ] |
| `onlinesales-ai/osmos-react-native-sdk` | ui | admin, write | [ ] |
| `onlinesales-ai/osmos-react-native-sdk-demo` | osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/osmos-ui-qa` | osmos-qa, ui | admin, write | [ ] |
| `onlinesales-ai/osmos-web-sdk` | osmos-client-delight, osmos-sdk, ui | admin, write | [ ] |
| `onlinesales-ai/osmos-web-sdk-playground` | osmos-sdk, ui | admin, write | [ ] |
| `onlinesales-ai/ott-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/paypal-web-internal-sdk` | ui | admin, write | [ ] |
| `onlinesales-ai/paypal-web-sdk` | ui | admin, write | [ ] |
| `onlinesales-ai/plaAdServer` | frigga-cloud, infra, osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/plaAdServer-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/placement-automation` | osmos-client-delight, ui | admin, write | [ ] |
| `onlinesales-ai/pmaxLauncher` | frigga-cloud, hyperlocal, infra, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/portfolioBidStrategyUpdater` | hyperlocal, osmos-offsite | admin, maintain | [ ] |
| `onlinesales-ai/propertySettingsSvcV2_frigga` | frigga-cloud, infra | admin | [ ] |
| `onlinesales-ai/publisher-svc` | frigga-cloud, infra, osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/python-cloud-function-template` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/reportService` | frigga-cloud, osmos-client-delight, osmos-media, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/reposilite-k8s` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/restAccessor` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/restAccessor4py3` | frigga-cloud | write | [ ] |
| `onlinesales-ai/restCommunicator` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/restObjects` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/retailer-service-api-qa` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/reusable-workflows` | frigga-cloud, infra | admin | [ ] |
| `onlinesales-ai/revXAdServerNodeV2` | frigga-cloud, infra, osmos-client-delight, osmos-media, osmos-performance | admin, write | [ ] |
| `onlinesales-ai/revXAdServerNodeV2-frigga` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/reviewService` | frigga-cloud, infra, osmos-client-delight | admin, write | [ ] |
| `onlinesales-ai/revxScripts` | cw-python, frigga-cloud, osmos-data | admin, write | [ ] |
| `onlinesales-ai/rmhc` | ui | admin, write | [ ] |
| `onlinesales-ai/rmhc-ui` | ui | admin, write | [ ] |
| `onlinesales-ai/rmhcReporting` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/rmhcTracking` | frigga-cloud, infra | admin, write | [ ] |
| `onlinesales-ai/scheduler-shared-dbaccess` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/schedulerLib4j` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/schedulerService` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/schedulerSvcObjects` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/shared-ui` | osmos-ui, ui, ui-team | admin, write | [ ] |
| `onlinesales-ai/smm-ui` | ui | maintain, write | [ ] |
| `onlinesales-ai/sofie-ai` | osmos-data, ui | write | [ ] |
| `onlinesales-ai/sofie-finance-agent` | osmos-data, ui | write | [ ] |
| `onlinesales-ai/sofie-keyword-suggestions-shared-util` | osmos-performance | write | [ ] |
| `onlinesales-ai/sofie-research-agent` | osmos-data, ui | write | [ ] |
| `onlinesales-ai/sofie-shared` | osmos-data, ui | write | [ ] |
| `onlinesales-ai/sokratiCache` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/statsLogger` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/statsLoggingClient` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/storeFeedSync` | osmos-client-delight, osmos-media, osmos-rms | admin, write | [ ] |
| `onlinesales-ai/strapi-hyperlocal` | ui | admin, write | [ ] |
| `onlinesales-ai/strapi-osmos` | ui | admin, write | [ ] |
| `onlinesales-ai/suchiService` | hyperlocal | admin, write | [ ] |
| `onlinesales-ai/temporalWorkflowTriggerConsumer` | frigga-cloud, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/test-backend` | osmos-media | admin, write | [ ] |
| `onlinesales-ai/third_party` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/tiktokLauncher` | osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/tiktokLauncher-temp` | osmos-offsite, osmso-offsite | write | [ ] |
| `onlinesales-ai/trackm` | frigga-cloud, osmos-client-delight, osmos-data | admin, write | [ ] |
| `onlinesales-ai/trackm-terraform` | frigga-cloud | admin | [ ] |
| `onlinesales-ai/trackmConfigs` | osmos-data | write | [ ] |
| `onlinesales-ai/ubidEmailPusher` | osmos-client-delight, osmos-media | admin, write | [ ] |
| `onlinesales-ai/ui-app-boilerplate` | ui | admin, write | [ ] |
| `onlinesales-ai/ui-domain-configs` | ui | admin | [ ] |
| `onlinesales-ai/ui-localium-domain-configs` | ui | admin | [ ] |
| `onlinesales-ai/ui-onboarding` | ui | admin, write | [ ] |
| `onlinesales-ai/ui-tools` | ui | admin, write | [ ] |
| `onlinesales-ai/uploader-ui` | osmos-rms | admin, write | [ ] |
| `onlinesales-ai/user-tagging-api-qa` | osmos-rms | write | [ ] |
| `onlinesales-ai/vendorUploader` | frigga-cloud, hyperlocal, osmos-offsite | admin, write | [ ] |
| `onlinesales-ai/web-osmos-sdk-source` | osmos-sdk | admin, write | [ ] |
| `onlinesales-ai/workflowEngine` | osmos-client-delight | maintain | [ ] |
| `onlinesales-ai/workload-identity-automation` | frigga-cloud | admin | [ ] |
| `GithubOrgPoliciesRestriction` | infra | admin | [ ] |
| `demo-repository` | ui | admin | [ ] |
