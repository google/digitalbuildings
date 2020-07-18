package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IFan;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.IDischarge;

public interface IDischarge_fan_run_status extends IField{

	public IRI iri();

    public void addComposedOfDischarge (IDischarge parameter);

	public Set<IDischarge> getComposedOfDischarge();

    public void addComposedOfFan (IFan parameter);

	public Set<IFan> getComposedOfFan();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}