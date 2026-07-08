from __future__ import annotations
import argparse
from .analyzer import analyze_file
from .report import print_console_report, write_json_report

def main(argv: list[str] | None=None) -> int:
    parser=argparse.ArgumentParser(prog='ref', description='REF Engine Alpha')
    sub=parser.add_subparsers(dest='command', required=True)
    analyze=sub.add_parser('analyze', help='Analyze a requirements document')
    analyze.add_argument('--input','-i', required=True, help='Input file (.xlsx, .docx, .md, .txt)')
    analyze.add_argument('--project','-p', required=False, help='Project configuration YAML')
    analyze.add_argument('--repo-root', required=False, help='Repository root')
    analyze.add_argument('--json-out', required=False, help='Write JSON report to file')
    analyze.add_argument('--max-examples', type=int, default=10)
    args=parser.parse_args(argv)
    if args.command=='analyze':
        report=analyze_file(args.input, project_path=args.project, repo_root=args.repo_root)
        print_console_report(report, max_examples=args.max_examples)
        if args.json_out:
            write_json_report(report,args.json_out); print(f"
JSON report written to: {args.json_out}")
        return 0
    parser.print_help(); return 1
if __name__=='__main__': raise SystemExit(main())
