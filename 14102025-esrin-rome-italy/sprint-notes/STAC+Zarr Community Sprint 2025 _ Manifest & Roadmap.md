---
title: 'STAC+Zarr Community Sprint 2025 : Manifest & Roadmap'

---

# STAC+Zarr Community Sprint 2025 : Manifest & Roadmap

**Event:** October 14-16, 2025 | ESA ESRIN, Frascati, Italy  
**Focus:** Advancing STAC-Zarr integration for cloud-native multidimensional geospatial data

---

## 🎯 Sprint Objectives

- Strengthen collaboration between STAC and Zarr communities
- Develop practical specification improvements for multidimensional data
- Address EOPF and Sentinel data representation challenges
- Share implementation experiences and identify ecosystem gaps

---

## 🏆 Key Achievements

### Specification Work

- [Best Practices for STAC Zarr and N-Dimensional Arrays](https://github.com/radiantearth/stac-best-practices/pull/29): Draft PR to be reviewed, approved and merged soon
- [Datacube proposal to replace variables with bands](https://github.com/stac-extensions/datacube/pull/32)
- [STAC Best practises for EOPF Zarr](https://github.com/EOPF-Sample-Service/eopf-stac) _specific PR to be linked_
- [STAC in Zarr](https://hackmd.io/@stac-sprint-2025/HJbMQV66le)

## 💬 Open Issues and Dicussions

- [STAC to handle storage implementation details and access parameters](https://github.com/radiantearth/stac-spec/discussions/1367)
- [GCPs reference for datasets that have `epsg` none, but have GCPs; also as issue for `geo-proj` zarr extension](https://github.com/stac-extensions/projection/issues/24)
- [Some various suggestions and issues for `eopf-stac` based on discussion](https://github.com/EOPF-Sample-Service/eopf-stac/issues)


---

## 🛣️ Roadmap & Next Steps

### Immediate Actions (November 2025)
- [ ] **Make the [Best Practices for STAC Zarr and N-Dimensional Arrays](https://github.com/radiantearth/stac-best-practices/pull/29) ready for review and merge** - _Owner: @emmanuelmathot_
- [ ] **Draft PR for [Datacube proposal to replace variables with bands: PR #32](https://github.com/stac-extensions/datacube/pull/32)** - _Owner: @rhysrevans3_
- [ ] **[STAC in Zarr](https://hackmd.io/@stac-sprint-2025/HJbMQV66le) new repo in https://github.com/zarr-experimental** - _Owner: ?_
- [ ] **Capture Multiscales discussions in a PR** - _Owner: @emmanuelmathot_
- [ ] **Capture chunk information in STAC**: It could go in the Zarr STAC Extension but it might be that this is a Zarr internal concern - _Owner: @christophreimer_

### Short-term Goals (Q4 2025 - Q1 2026)
- [ ] **Pursue the discussion around [STAC to handle storage implementation details and access parameters](https://github.com/radiantearth/stac-spec/discussions/1367) in STAC Community Meetup** - _Lead: @emmanuelmathot_
- [ ] **Adopt best practices for EOPF and provide reference implementation in [eopf-stac](https://github.com/EOPF-Sample-Service/eopf-stac)** - _Lead: EOPF Sample Service project_
- [ ] **Goal 3** - _Lead: [Name/Org]_

### Long-term Vision (2026)
- [ ] **Vision item 1**
- [ ] **Vision item 2**
- [ ] **Vision item 3**

---

## 📚 Resources

### Specification Repositories
- [STAC Specification](https://github.com/radiantearth/stac-spec)
- [STAC Best Practises](https://github.com/radiantearth/stac-best-practices)
- [STAC API Specification](https://github.com/radiantearth/stac-api-spec)
- [STAC Extensions](https://github.com/stac-extensions)
- [GeoZarr Specification](https://github.com/zarr-developers/geozarr-spec)

### Sprint Documentation
- [Sprint Preparation Topics](https://github.com/radiantearth/community-sprints/blob/main/14102025-esrin-rome-italy/prep-work/specification-topics.md)
- [Sprint Agenda](https://github.com/radiantearth/community-sprints/blob/main/14102025-esrin-rome-italy/agenda.md)

### Community Channels
- Zarr Community: [zarr.dev/community](https://zarr.dev/community/)
- [STAC Community Sprint CNG channel](https://cloudnativegeo.slack.com/archives/C094EKRDY04)

---

## 🙏 Acknowledgments

### Participants

_[Put your name, org and github handle]_

Emmanuel Mathot, Development Seed, @emmanuelmathot
Daniel Santillan, EOX IT Services GmbH, @santilland
Petr Sevcik, EOX IT Services GmbH, @scartography
Michele Claus, Eurac Research, @clausmichele
Mario Winkler, DLR, @mario-winkler
Lukas Bindreiter, Tilebox, @lukasbindreiter
Fabrice Brito, Terradue, @fabricebrito
Rhys Evans, CEDA, @rhysrevans3
Julia Signell, Element 84, @jsignell
Florian Ziemen, DKRZ, @florianziemen
Vincent Dumoulin, ESA, @dumvin
Kameswar Rao Modali, DKRZ, @kmodali
Catherine Bouzinac, CSGF, @cbouzina
Brian Terry, CEOS-SEO, @brianterry-ama
Christoph Reimer, EODC, @christophreimer

### Sponsors & Hosts
- **ESA ESRIN** - Venue host and logistics support
- **Development Seed** - Social event sponsor

---

## Feedback

[form](https://forms.gle/NjHRdMW2bP9eB5We9)

## 📝 Notes

_Space for additional observations, insights, or community feedback from the sprint_

---
