package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IStatus;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;
import www.google.com.digitalbuildings._0_0_1.subfields.IDryer;

public interface IDryer_run_status_8 extends IField{

	public IRI iri();

    public void addComposedOfDryer (IDryer parameter);

	public Set<IDryer> getComposedOfDryer();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

    public void addComposedOfStatus (IStatus parameter);

	public Set<IStatus> getComposedOfStatus();

}