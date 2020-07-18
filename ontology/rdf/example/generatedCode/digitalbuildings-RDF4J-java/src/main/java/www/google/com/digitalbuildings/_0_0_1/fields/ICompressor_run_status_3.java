package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.ICompressor;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;

public interface ICompressor_run_status_3 extends IField{

	public IRI iri();

    public void addComposedOfCompressor (ICompressor parameter);

	public Set<ICompressor> getComposedOfCompressor();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}