package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IMode;
import www.google.com.digitalbuildings._0_0_1.subfields.IRun;

public interface IRun_mode extends IField{

	public IRI iri();

    public void addComposedOfMode (IMode parameter);

	public Set<IMode> getComposedOfMode();

    public void addComposedOfRun (IRun parameter);

	public Set<IRun> getComposedOfRun();

}