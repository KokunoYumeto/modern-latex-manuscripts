#!/usr/bin/env python3
"""Reduce the live EGA landing metadata to readers, coverage, and caveats."""

from pathlib import Path

import edit_ega_reader_first_metadata_zenodo_20260731 as edit


edit.OLD_DESCRIPTION_SHA256 = (
    "593574CA314620FED101D837C66278317C512DD5B32ACC452355598E1119DE8E"
)
edit.DESCRIPTION = """<p><strong>Start here:</strong> download <code>00 Current_EGA_English_Readers_and_Buildable_TeX_20260730.zip</code> for the current cumulative English readers and their buildable TeX. The reader PDFs and master TeX files are also available individually; EGA 0 is the default preview.</p>
<p><strong>Coverage:</strong> EGA 0 is complete through Section 13; EGA I and II are complete through their authority EOFs; EGA III contains the complete published text through Section 7.9.14; and the cumulative EGA IV reader covers Sections 1-10. Separate bounded readers cover EGA IV Sections 16-18 and Sections 19-21 with Part 4 backmatter. Sections 11-15 remain the cumulative EGA IV integration gap.</p>
<p>These are scholarly working translations, not critical editions, peer-review or mathematical certifications, rights determinations, whole-EGA completion claims, or tagged-PDF accessibility remediation. No blanket license or transfer of underlying rights is asserted.</p>"""
edit.NOTES = ""
edit.RECEIPT_PATH = Path(edit.REPO_ROOT) / "manifests" / "published-zenodo" / (
    "20260731_ega_record_21717450_readers_only_metadata_revision.json"
)


def validate_readers_only_metadata(metadata: dict) -> None:
    if metadata.get("description") != edit.DESCRIPTION:
        raise RuntimeError("EGA readers-only description did not persist")
    if len(edit.DESCRIPTION.encode("utf-8")) > 1_200:
        raise RuntimeError("EGA readers-only description grew beyond its boundary")
    if edit.DESCRIPTION.count("<p>") != 3:
        raise RuntimeError("EGA readers-only description must have three paragraphs")
    lowered = edit.DESCRIPTION.casefold()
    for forbidden in (
        "image",
        "raster",
        "dpi",
        "witness",
        "crop",
        "png",
        "qa archive",
    ):
        if forbidden in lowered:
            raise RuntimeError(f"EGA description contains secondary-image prose: {forbidden}")
    if metadata.get("additional_descriptions"):
        raise RuntimeError("EGA landing page still has an additional notes speech")


def replacement_metadata(metadata: dict) -> dict:
    updated = edit.copy.deepcopy(metadata)
    updated["description"] = edit.DESCRIPTION
    updated["subjects"] = [
        row
        for row in updated.get("subjects", [])
        if row.get("subject") not in edit.IMAGE_ONLY_SUBJECTS
    ]
    updated["additional_descriptions"] = []
    return updated


edit.validate_reader_first_metadata = validate_readers_only_metadata
edit.replacement_metadata = replacement_metadata


if __name__ == "__main__":
    edit.main()
